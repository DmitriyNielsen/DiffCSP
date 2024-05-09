import time
import argparse
import torch

from tqdm import tqdm
from torch.optim import Adam
from pathlib import Path
from types import SimpleNamespace
from torch_geometric.data import Batch

from eval_utils import load_model, lattices_to_params_shape, recommand_step_lr

from pymatgen.core.structure import Structure
from pymatgen.core.lattice import Lattice
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pyxtal.symmetry import Group

import copy

import numpy as np


def diffusion(loader, model, num_evals, step_lr=1e-5):
    # Initialize lists to store outputs
    frac_coords = []
    num_atoms = []
    atom_types = []
    lattices = []
    input_data_list = []

    # Fetch the first batch only
    first_batch = next(iter(loader))
    if torch.cuda.is_available():
        first_batch.cuda()

    # Run the process only for the first batch
    batch_all_frac_coords = []
    batch_all_lattices = []
    batch_frac_coords, batch_num_atoms, batch_atom_types = [], [], []
    batch_lattices = []

    # Print and process for each eval
    for eval_idx in range(num_evals):
        print(f'Using first batch, sample {eval_idx} / {num_evals}')
        outputs, traj = model.sample(first_batch, step_lr=step_lr)
        batch_frac_coords.append(outputs['frac_coords'].detach().cpu())
        batch_num_atoms.append(outputs['num_atoms'].detach().cpu())
        batch_atom_types.append(outputs['atom_types'].detach().cpu())
        batch_lattices.append(outputs['lattices'].detach().cpu())

    # Aggregate results from the evals
    frac_coords.append(torch.stack(batch_frac_coords, dim=0))
    num_atoms.append(torch.stack(batch_num_atoms, dim=0))
    atom_types.append(torch.stack(batch_atom_types, dim=0))
    lattices.append(torch.stack(batch_lattices, dim=0))
    
    # Since we're only using one batch, we convert this single batch to a data list directly
    input_data_list = first_batch.to_data_list()

    # Concatenate all outputs for final results
    frac_coords = torch.cat(frac_coords, dim=1)
    num_atoms = torch.cat(num_atoms, dim=1)
    atom_types = torch.cat(atom_types, dim=1)
    lattices = torch.cat(lattices, dim=1)
    lengths, angles = lattices_to_params_shape(lattices)
    input_data_batch = Batch.from_data_list(input_data_list)

    # Return the processed data
    return (
        frac_coords, atom_types, lattices, lengths, angles, num_atoms, input_data_batch
    )




def main(args):
    # load_data if do reconstruction.
    model_path = Path(args.model_path)
    model, test_loader, cfg = load_model(
        model_path, load_data=True)

    if torch.cuda.is_available():
        model.to('cuda')


    print('Evaluate the diffusion model.')

    step_lr = args.step_lr if args.step_lr >= 0 else recommand_step_lr['csp' if args.num_evals == 1 else 'csp_multi'][args.dataset]


    start_time = time.time()
    (frac_coords, atom_types, lattices, lengths, angles, num_atoms, input_data_batch) = diffusion(
        test_loader, model, args.num_evals, step_lr)

    if args.label == '':
        diff_out_name = 'eval_diff.pt'
    else:
        diff_out_name = f'eval_diff_{args.label}.pt'

    torch.save({
        'eval_setting': args,
        'input_data_batch': input_data_batch,
        'frac_coords': frac_coords,
        'num_atoms': num_atoms,
        'atom_types': atom_types,
        'lattices': lattices,
        'lengths': lengths,
        'angles': angles,
        'time': time.time() - start_time,
    }, model_path / diff_out_name)    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', required=True)
    parser.add_argument('--dataset', required=True)
    parser.add_argument('--step_lr', default=-1, type=float)
    parser.add_argument('--num_evals', default=1, type=int)
    parser.add_argument('--label', default='')
    args = parser.parse_args()
    main(args)
