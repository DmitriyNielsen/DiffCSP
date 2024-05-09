AWARE: git is set to folder: /Users/dmitriynielsen/GitHub/DiffCSP/New_try02/DiffCSP/.git - everything before will not be pushed / version control.

Hydra loads the "default.yaml" file from the "conf" directory, and any values in this file are accessible as attributes of the cfg object.


.
├── LICENSE
├── README.md
├── conf
│   ├── data
│   │   ├── carbon_24.yaml
│   │   ├── mp_20.yaml
│   │   ├── mpts_52.yaml
│   │   └── perov_5.yaml
│   ├── default.yaml
│   ├── logging
│   │   ├── default.yaml
│   │   ├── default.yaml.orig
│   │   └── default.yaml.rej
│   ├── model
│   │   ├── beta_scheduler
│   │   │   └── cosine.yaml
│   │   ├── decoder
│   │   │   └── cspnet.yaml
│   │   ├── diffusion.yaml
│   │   ├── diffusion_w_type.yaml
│   │   ├── energy.yaml
│   │   └── sigma_scheduler
│   │       └── wrapped.yaml
│   ├── optim
│   │   ├── default.yaml
│   │   ├── default.yaml.orig
│   │   ├── default.yaml.rej
│   │   └── default.yaml.rej.orig
│   └── train
│       └── default.yaml
├── data
│   ├── carbon_24
│   │   ├── test.csv
│   │   ├── train.csv
│   │   └── val.csv
│   ├── mp_20
│   │   ├── test.csv
│   │   ├── train.csv
│   │   └── val.csv
│   ├── mpts_52
│   │   ├── test.csv
│   │   ├── train.csv
│   │   └── val.csv
│   └── perov_5
│       ├── test.csv
│       ├── test_ori.pt
│       ├── train.csv
│       ├── train_ori.pt
│       ├── val.csv
│       └── val_ori.pt
├── diffcsp
│   ├── __init__.py
│   ├── __pycache__
│   │   └── __init__.cpython-311.pyc
│   ├── common
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── data_utils.cpython-311.pyc
│   │   │   └── utils.cpython-311.pyc
│   │   ├── constants.py
│   │   ├── data_utils.py
│   │   └── utils.py
│   ├── pl_data
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── datamodule.cpython-311.pyc
│   │   │   └── dataset.cpython-311.pyc
│   │   ├── datamodule.py
│   │   └── dataset.py
│   ├── pl_modules
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── cspnet.cpython-311.pyc
│   │   │   ├── diff_utils.cpython-311.pyc
│   │   │   └── diffusion.cpython-311.pyc
│   │   ├── cspnet.py
│   │   ├── diff_utils.py
│   │   ├── diffusion.py
│   │   ├── diffusion_w_type.py
│   │   ├── energy_model.py
│   │   ├── gnn.py
│   │   └── model.py
│   ├── prop_models
│   │   ├── carbon
│   │   │   ├── epoch=2364-step=56759.ckpt
│   │   │   ├── hparams.yaml
│   │   │   ├── lattice_scaler.pt
│   │   │   └── prop_scaler.pt
│   │   ├── mp20
│   │   │   ├── epoch=839-step=89039.ckpt
│   │   │   ├── hparams.yaml
│   │   │   ├── lattice_scaler.pt
│   │   │   └── prop_scaler.pt
│   │   └── perovskite
│   │       ├── epoch=2664-step=61294.ckpt
│   │       ├── hparams.yaml
│   │       ├── lattice_scaler.pt
│   │       └── prop_scaler.pt
│   └── run.py
├── fig
│   ├── demo.gif
│   └── overview.png
├── hydra
│   └── singlerun
│       ├── 2024-04-22
│       │   ├── bob123
│       │   │   ├── epoch=0-step=12.ckpt
│       │   │   ├── hparams.yaml
│       │   │   ├── lattice_scaler.pt
│       │   │   ├── prop_scaler.pt
│       │   │   ├── run.log
│       │   │   └── wandb
│       │   │       ├── debug-internal.log -> run-20240422_170516-g3fxa1ad/logs/debug-internal.log
│       │   │       ├── debug.log -> run-20240422_170516-g3fxa1ad/logs/debug.log
│       │   │       ├── latest-run -> run-20240422_170516-g3fxa1ad
│       │   │       └── run-20240422_170516-g3fxa1ad
│       │   │           ├── files
│       │   │           │   ├── config.yaml
│       │   │           │   ├── output.log
│       │   │           │   ├── requirements.txt
│       │   │           │   ├── wandb-metadata.json
│       │   │           │   └── wandb-summary.json
│       │   │           ├── logs
│       │   │           │   ├── debug-internal.log
│       │   │           │   └── debug.log
│       │   │           ├── run-g3fxa1ad.wandb
│       │   │           └── tmp
│       │   │               └── code
│       │   ├── bob1234
│       │   │   ├── epoch=0-step=12.ckpt
│       │   │   ├── hparams.yaml
│       │   │   ├── lattice_scaler.pt
│       │   │   ├── prop_scaler.pt
│       │   │   ├── run.log
│       │   │   └── wandb
│       │   │       ├── debug-internal.log -> run-20240422_171111-idyy9h6w/logs/debug-internal.log
│       │   │       ├── debug.log -> run-20240422_171111-idyy9h6w/logs/debug.log
│       │   │       ├── latest-run -> run-20240422_171111-idyy9h6w
│       │   │       └── run-20240422_171111-idyy9h6w
│       │   │           ├── files
│       │   │           │   ├── config.yaml
│       │   │           │   ├── output.log
│       │   │           │   ├── requirements.txt
│       │   │           │   ├── wandb-metadata.json
│       │   │           │   └── wandb-summary.json
│       │   │           ├── logs
│       │   │           │   ├── debug-internal.log
│       │   │           │   └── debug.log
│       │   │           ├── run-idyy9h6w.wandb
│       │   │           └── tmp
│       │   │               └── code
│       │   ├── bob12346
│       │   │   ├── epoch=0-step=12.ckpt
│       │   │   ├── hparams.yaml
│       │   │   ├── lattice_scaler.pt
│       │   │   ├── prop_scaler.pt
│       │   │   ├── run.log
│       │   │   └── wandb
│       │   │       ├── debug-internal.log -> run-20240422_171545-r7mman9h/logs/debug-internal.log
│       │   │       ├── debug.log -> run-20240422_171545-r7mman9h/logs/debug.log
│       │   │       ├── latest-run -> run-20240422_171545-r7mman9h
│       │   │       └── run-20240422_171545-r7mman9h
│       │   │           ├── files
│       │   │           │   ├── config.yaml
│       │   │           │   ├── output.log
│       │   │           │   ├── requirements.txt
│       │   │           │   ├── wandb-metadata.json
│       │   │           │   └── wandb-summary.json
│       │   │           ├── logs
│       │   │           │   ├── debug-internal.log
│       │   │           │   └── debug.log
│       │   │           ├── run-r7mman9h.wandb
│       │   │           └── tmp
│       │   │               └── code
│       │   ├── bob123467
│       │   │   ├── epoch=0-step=12.ckpt
│       │   │   ├── hparams.yaml
│       │   │   ├── lattice_scaler.pt
│       │   │   ├── prop_scaler.pt
│       │   │   ├── run.log
│       │   │   └── wandb
│       │   │       ├── debug-internal.log -> run-20240422_171848-7bqxylhd/logs/debug-internal.log
│       │   │       ├── debug.log -> run-20240422_171848-7bqxylhd/logs/debug.log
│       │   │       ├── latest-run -> run-20240422_171848-7bqxylhd
│       │   │       └── run-20240422_171848-7bqxylhd
│       │   │           ├── files
│       │   │           │   ├── config.yaml
│       │   │           │   ├── output.log
│       │   │           │   ├── requirements.txt
│       │   │           │   ├── wandb-metadata.json
│       │   │           │   └── wandb-summary.json
│       │   │           ├── logs
│       │   │           │   ├── debug-internal.log
│       │   │           │   └── debug.log
│       │   │           ├── run-7bqxylhd.wandb
│       │   │           └── tmp
│       │   │               └── code
│       │   ├── bob1234678
│       │   │   ├── epoch=0-step=12.ckpt
│       │   │   ├── hparams.yaml
│       │   │   ├── lattice_scaler.pt
│       │   │   ├── prop_scaler.pt
│       │   │   ├── run.log
│       │   │   └── wandb
│       │   │       ├── debug-internal.log -> run-20240422_172117-m9jy82v7/logs/debug-internal.log
│       │   │       ├── debug.log -> run-20240422_172117-m9jy82v7/logs/debug.log
│       │   │       ├── latest-run -> run-20240422_172117-m9jy82v7
│       │   │       └── run-20240422_172117-m9jy82v7
│       │   │           ├── files
│       │   │           │   ├── config.yaml
│       │   │           │   ├── output.log
│       │   │           │   ├── requirements.txt
│       │   │           │   ├── wandb-metadata.json
│       │   │           │   └── wandb-summary.json
│       │   │           ├── logs
│       │   │           │   ├── debug-internal.log
│       │   │           │   └── debug.log
│       │   │           ├── run-m9jy82v7.wandb
│       │   │           └── tmp
│       │   │               └── code
│       │   ├── exp_04
│       │   │   ├── epoch=0-step=12.ckpt
│       │   │   ├── epoch=1-step=24.ckpt
│       │   │   ├── hparams.yaml
│       │   │   ├── lattice_scaler.pt
│       │   │   ├── prop_scaler.pt
│       │   │   └── run.log
│       │   └── perov01
│       │       ├── hparams.yaml
│       │       ├── lattice_scaler.pt
│       │       ├── prop_scaler.pt
│       │       └── run.log
│       ├── 2024-04-23
│       │   └── exp_04
│       │       ├── epoch=0-step=12.ckpt
│       │       ├── hparams.yaml
│       │       ├── lattice_scaler.pt
│       │       ├── prop_scaler.pt
│       │       └── run.log
│       └── 2024-04-24
│           └── exp_04
│               ├── epoch=0-step=12.ckpt
│               ├── hparams.yaml
│               ├── lattice_scaler.pt
│               ├── prop_scaler.pt
│               └── run.log
├── scripts
│   ├── compute_metrics.py
│   ├── eval_utils.py
│   ├── evaluate.py
│   ├── generation.py
│   ├── optimization.py
│   └── sample.py
└── wandb
    ├── debug-internal.log -> run-20240424_175905-s6ujh2xy/logs/debug-internal.log
    ├── debug.log -> run-20240424_175905-s6ujh2xy/logs/debug.log
    ├── latest-run -> run-20240424_175905-s6ujh2xy
    ├── run-20240422_233447-hov6rwpn
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   ├── wandb-metadata.json
    │   │   └── wandb-summary.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-hov6rwpn.wandb
    │   └── tmp
    │       └── code
    ├── run-20240422_233516-iuwcium9
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   ├── wandb-metadata.json
    │   │   └── wandb-summary.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-iuwcium9.wandb
    │   └── tmp
    │       └── code
    ├── run-20240422_235526-xh1k1duj
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   ├── wandb-metadata.json
    │   │   └── wandb-summary.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-xh1k1duj.wandb
    │   └── tmp
    │       └── code
    ├── run-20240423_212729-acg8prba
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   └── wandb-metadata.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-acg8prba.wandb
    │   └── tmp
    │       └── code
    ├── run-20240423_215004-4c1gba9w
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   ├── wandb-metadata.json
    │   │   └── wandb-summary.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-4c1gba9w.wandb
    │   └── tmp
    │       └── code
    ├── run-20240423_215353-kuo75bu1
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   └── wandb-metadata.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-kuo75bu1.wandb
    │   └── tmp
    │       └── code
    ├── run-20240424_002942-10vha8il
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   └── wandb-metadata.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-10vha8il.wandb
    │   └── tmp
    │       └── code
    ├── run-20240424_134546-e0258idf
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   ├── wandb-metadata.json
    │   │   └── wandb-summary.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-e0258idf.wandb
    │   └── tmp
    │       └── code
    ├── run-20240424_134643-9vyfwzte
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   ├── wandb-metadata.json
    │   │   └── wandb-summary.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-9vyfwzte.wandb
    │   └── tmp
    │       └── code
    ├── run-20240424_134751-tzglvzqs
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   ├── wandb-metadata.json
    │   │   └── wandb-summary.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-tzglvzqs.wandb
    │   └── tmp
    │       └── code
    ├── run-20240424_134841-w01q700t
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   └── wandb-metadata.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-w01q700t.wandb
    │   └── tmp
    │       └── code
    ├── run-20240424_135814-vcwz8ybo
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   └── wandb-metadata.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-vcwz8ybo.wandb
    │   └── tmp
    │       └── code
    ├── run-20240424_135946-gbqtyxzv
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   └── wandb-metadata.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-gbqtyxzv.wandb
    │   └── tmp
    │       └── code
    ├── run-20240424_140501-nymqf2ve
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   └── wandb-metadata.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-nymqf2ve.wandb
    │   └── tmp
    │       └── code
    ├── run-20240424_140658-elp36lxo
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   └── wandb-metadata.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-elp36lxo.wandb
    │   └── tmp
    │       └── code
    ├── run-20240424_141115-bqvxio80
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   └── wandb-metadata.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-bqvxio80.wandb
    │   └── tmp
    │       └── code
    ├── run-20240424_143245-oq2navct
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   ├── wandb-metadata.json
    │   │   └── wandb-summary.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-oq2navct.wandb
    │   └── tmp
    │       └── code
    ├── run-20240424_143509-zdgtkpm5
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   └── wandb-metadata.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-zdgtkpm5.wandb
    │   └── tmp
    │       └── code
    ├── run-20240424_162625-w5pzbact
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   └── wandb-metadata.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-w5pzbact.wandb
    │   └── tmp
    │       └── code
    ├── run-20240424_163029-rqipelfx
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   └── wandb-metadata.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-rqipelfx.wandb
    │   └── tmp
    │       └── code
    ├── run-20240424_163235-wc6xmdq7
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   └── wandb-metadata.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-wc6xmdq7.wandb
    │   └── tmp
    │       └── code
    ├── run-20240424_163617-thojyhu6
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   ├── wandb-metadata.json
    │   │   └── wandb-summary.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-thojyhu6.wandb
    │   └── tmp
    │       └── code
    ├── run-20240424_163906-tyv4tytd
    │   ├── files
    │   │   ├── config.yaml
    │   │   ├── output.log
    │   │   ├── requirements.txt
    │   │   └── wandb-metadata.json
    │   ├── logs
    │   │   ├── debug-internal.log
    │   │   └── debug.log
    │   ├── run-tyv4tytd.wandb
    │   └── tmp
    │       └── code
    └── run-20240424_175905-s6ujh2xy
        ├── files
        │   ├── config.yaml
        │   ├── output.log
        │   ├── requirements.txt
        │   ├── wandb-metadata.json
        │   └── wandb-summary.json
        ├── logs
        │   ├── debug-internal.log
        │   └── debug.log
        ├── run-s6ujh2xy.wandb
        └── tmp
            └── code

200 directories, 359 files


(diffcsp_2204)  dmitriynielsen@Dmitriys-MBP New_try02 % 
 cd /Users/dmitriynielsen/GitHub/DiffCSP/New_try02 ; /usr/bin/env /Users/dmitriynielsen/GitHub/DiffCSP/New_try02/diffcsp_2204/bin/python /Users/dmitriynielsen/.vscode/e
(diffcsp_2204)  dmitriynielsen@Dmitriys-MBP New_try02 %  cd /Users/dmitriynielsen/Gi
tHub/DiffCSP/New_try02 ; /usr/bin/env /Users/dmitriynielsen/GitHub/DiffCSP/New_try02
/diffcsp_2204/bin/python /Users/dmitriynielsen/.vscode/extensions/ms-python.debugpy-
2024.4.0-darwin-arm64/bundled/libs/debugpy/adapter/../../debugpy/launcher 60543 -- /
Users/dmitriynielsen/GitHub/DiffCSP/New_try02/DiffCSP/scripts/sample.py --model_path
 /Users/dmitriynielsen/GitHub/DiffCSP/New_try02/DiffCSP/diffcsp/prop_models/perovski
te --save_path /Users/dmitriynielsen/GitHub/DiffCSP/New_try02/DiffCSP/diffcsp/Saved_
tests --formula SiO2 --num_evals 5 
Backend MacOSX is interactive backend. Turning interactive mode on.