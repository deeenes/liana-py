# LIANA: a LIgand-receptor ANalysis frAmework <img src="https://github.com/saezlab/liana-py/blob/main/docs/source/logo.png?raw=true" align="right" height="125">

<!-- badges: start -->
[![main](https://github.com/saezlab/liana-py/actions/workflows/main.yml/badge.svg)](https://github.com/saezlab/liana-py/actions)
[![GitHub issues](https://img.shields.io/github/issues/saezlab/liana-py.svg)](https://github.com/saezlab/liana-py/issues/)
[![Documentation Status](https://readthedocs.org/projects/liana-py/badge/?version=latest)](https://liana-py.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/saezlab/liana-py/branch/main/graph/badge.svg?token=TM0P29KKN5)](https://codecov.io/gh/saezlab/liana-py)
<!-- badges: end -->


LIANA is a Ligand-Receptor inference framework that enables the use of any LR method with any resource.
This is its faster and memory efficient Python implementation, an R version is also available [here](https://github.com/saezlab/liana).


### *liana-py is still under heavy development - a stable alpha release will be created soon*


For further information please check LIANA's [documentation](), and also [tutorial]().

## Install LIANA
```
pip install git+https://github.com/saezlab/liana-py
```

## Methods

The methods implemented in this repository are:

- [CellPhoneDBv2](https://github.com/Teichlab/cellphonedb)
- [NATMI](https://github.com/forrest-lab/NATMI)
- [Connectome](https://github.com/msraredon/Connectome)
- [SingleCellSignalR](https://github.com/SCA-IRCM/SingleCellSignalR)
- *1-vs-rest* expression LogFC score
- `rank_aggregate` of the predictions calculated with the
[RobustRankAggregate](https://academic.oup.com/bioinformatics/article/28/4/573/213339) method


TO be included:
- [CellChat](https://github.com/sqjin/CellChat)
- Geometric mean + perms



## Ligand-Receptor Resources

The following CCC resources are accessible via this pipeline:

- Consensus ($)
- CellCall
- CellChatDB
- CellPhoneDB
- Ramilowski2015
- Baccin2019
- LRdb
- Kiroauc2010
- ICELLNET
- iTALK
- EMBRACE
- HPMR
- Guide2Pharma
- ConnectomeDB2020
- CellTalkDB

($) LIANA's default `Consensus` resource was generated from several expert-curated resources, 
filtered to additional quality control steps including literature support, complex re-union/consensus,
and localisation.


## Cite LIANA:

Dimitrov, D., Türei, D., Garrido-Rodriguez M., Burmedi P.L., Nagai, J.S., Boys, C., Flores, R.O.R., Kim, H., Szalai, B., Costa, I.G., Valdeolivas, A., Dugourd, A. and Saez-Rodriguez, J. Comparison of methods and resources for cell-cell communication inference from single-cell RNA-Seq data. Nat Commun 13, 3224 (2022). https://doi.org/10.1038/s41467-022-30755-0
Also, if you use the OmniPath CCC Resource for your analysis, please cite:

Türei, D., Valdeolivas, A., Gul, L., Palacio‐Escat, N., Klein, M., Ivanova, O., Ölbei, M., Gábor, A., Theis, F., Módos, D. and Korcsmáros, T., 2021. Integrated intra‐and intercellular signaling knowledge for multicellular omics analysis. Molecular systems biology, 17(3), p.e9923. https://doi.org/10.15252/msb.20209923

Similarly, please consider citing any of the methods and/or resources implemented in liana, that were particularly relevant for your research!


