# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/nkapila6/mlrose-ky/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                                      |    Stmts |     Miss |   Cover |   Missing |
|---------------------------------------------------------- | -------: | -------: | ------: | --------: |
| mlrose\_ky/\_\_init\_\_.py                                |       19 |        0 |    100% |           |
| mlrose\_ky/algorithms/\_\_init\_\_.py                     |        9 |        0 |    100% |           |
| mlrose\_ky/algorithms/crossovers/\_\_init\_\_.py          |        3 |        0 |    100% |           |
| mlrose\_ky/algorithms/crossovers/\_crossover\_base.py     |       10 |        1 |     90% |        71 |
| mlrose\_ky/algorithms/crossovers/one\_point\_crossover.py |       10 |        0 |    100% |           |
| mlrose\_ky/algorithms/crossovers/tsp\_crossover.py        |       48 |       31 |     35% |85, 109-147 |
| mlrose\_ky/algorithms/crossovers/uniform\_crossover.py    |       11 |        0 |    100% |           |
| mlrose\_ky/algorithms/decay/\_\_init\_\_.py               |        4 |        0 |    100% |           |
| mlrose\_ky/algorithms/decay/arithmetic\_decay.py          |       28 |       13 |     54% |50, 52, 54, 57, 64, 67-69, 109-121 |
| mlrose\_ky/algorithms/decay/custom\_decay.py              |       21 |       10 |     52% |37, 40, 43-45, 79-90 |
| mlrose\_ky/algorithms/decay/exponential\_decay.py         |       29 |       13 |     55% |52, 54, 56, 59, 66, 69-71, 110-122 |
| mlrose\_ky/algorithms/decay/geometric\_decay.py           |       28 |       13 |     54% |50, 52, 54, 57, 64, 67-69, 108-120 |
| mlrose\_ky/algorithms/ga.py                               |       99 |       33 |     67% |29, 48, 79-91, 176, 178, 180, 182, 184, 186, 198, 208-212, 220-221, 252-253, 269, 273-274, 287-288, 292 |
| mlrose\_ky/algorithms/gd.py                               |       48 |       10 |     79% |62, 64, 66, 70, 79, 108, 112-113, 124, 133 |
| mlrose\_ky/algorithms/hc.py                               |       55 |       14 |     75% |67, 69, 71, 95-97, 110, 114-126, 140-141, 145, 150 |
| mlrose\_ky/algorithms/mimic.py                            |       54 |       12 |     78% |78, 80, 82, 84, 86, 88, 102, 141, 145-146, 158, 164 |
| mlrose\_ky/algorithms/mutators/\_\_init\_\_.py            |        4 |        0 |    100% |           |
| mlrose\_ky/algorithms/mutators/\_mutator\_base.py         |       11 |        1 |     91% |        62 |
| mlrose\_ky/algorithms/mutators/discrete\_mutator.py       |       17 |       11 |     35% |33-34, 55-66 |
| mlrose\_ky/algorithms/mutators/gene\_swap\_mutator.py     |       11 |        0 |    100% |           |
| mlrose\_ky/algorithms/mutators/single\_gene\_mutator.py   |       14 |        6 |     57% |     58-65 |
| mlrose\_ky/algorithms/mutators/single\_shift\_mutator.py  |       14 |        8 |     43% |33-34, 54-60 |
| mlrose\_ky/algorithms/rhc.py                              |       64 |       17 |     73% |71, 73, 75, 77, 103-105, 133-136, 140-153, 161, 165, 170 |
| mlrose\_ky/algorithms/sa.py                               |       50 |        8 |     84% |72, 74, 76, 92, 109, 133-134, 147 |
| mlrose\_ky/decorators/\_\_init\_\_.py                     |        1 |        0 |    100% |           |
| mlrose\_ky/decorators/short\_name\_decorator.py           |       12 |        2 |     83% |     56-57 |
| mlrose\_ky/fitness/\_\_init\_\_.py                        |       10 |        0 |    100% |           |
| mlrose\_ky/fitness/\_discrete\_peaks\_base.py             |       14 |        2 |     86% |    38, 66 |
| mlrose\_ky/fitness/continuous\_peaks.py                   |       33 |        3 |     91% |45, 105, 124 |
| mlrose\_ky/fitness/custom\_fitness.py                     |       15 |        3 |     80% |59, 84, 96 |
| mlrose\_ky/fitness/flip\_flop.py                          |       20 |        6 |     70% | 52, 77-82 |
| mlrose\_ky/fitness/four\_peaks.py                         |       20 |        2 |     90% |    65, 86 |
| mlrose\_ky/fitness/knapsack.py                            |       30 |        6 |     80% |72, 74, 76, 78, 104, 106 |
| mlrose\_ky/fitness/max\_k\_color.py                       |       18 |        2 |     89% |    92, 98 |
| mlrose\_ky/fitness/one\_max.py                            |       11 |        1 |     91% |        53 |
| mlrose\_ky/fitness/queens.py                              |       36 |        8 |     78% |72, 95, 116, 144-150 |
| mlrose\_ky/fitness/six\_peaks.py                          |       23 |        2 |     91% |    67, 88 |
| mlrose\_ky/fitness/travelling\_salesperson.py             |       54 |        8 |     85% |58, 81, 83, 85, 110, 112, 114, 116 |
| mlrose\_ky/generators/\_\_init\_\_.py                     |        9 |        0 |    100% |           |
| mlrose\_ky/generators/continuous\_peaks\_generator.py     |       15 |        0 |    100% |           |
| mlrose\_ky/generators/flip\_flop\_generator.py            |       10 |        0 |    100% |           |
| mlrose\_ky/generators/four\_peaks\_generator.py           |       13 |        0 |    100% |           |
| mlrose\_ky/generators/knapsack\_generator.py              |       24 |        0 |    100% |           |
| mlrose\_ky/generators/max\_k\_color\_generator.py         |       38 |        4 |     89% |     93-98 |
| mlrose\_ky/generators/one\_max\_generator.py              |       13 |        0 |    100% |           |
| mlrose\_ky/generators/queens\_generator.py                |       14 |        0 |    100% |           |
| mlrose\_ky/generators/six\_peaks\_generator.py            |       13 |        0 |    100% |           |
| mlrose\_ky/generators/tsp\_generator.py                   |       45 |        7 |     84% |62-67, 103 |
| mlrose\_ky/gridsearch/\_\_init\_\_.py                     |        1 |        0 |    100% |           |
| mlrose\_ky/gridsearch/grid\_search\_mixin.py              |       33 |        2 |     94% |   128-129 |
| mlrose\_ky/neural/\_\_init\_\_.py                         |        7 |        0 |    100% |           |
| mlrose\_ky/neural/\_nn\_base.py                           |       64 |        3 |     95% |39, 56, 82 |
| mlrose\_ky/neural/activation/\_\_init\_\_.py              |        6 |        0 |    100% |           |
| mlrose\_ky/neural/activation/identity.py                  |       10 |        0 |    100% |           |
| mlrose\_ky/neural/activation/leaky\_relu.py               |       12 |        0 |    100% |           |
| mlrose\_ky/neural/activation/relu.py                      |       11 |        0 |    100% |           |
| mlrose\_ky/neural/activation/sigmoid.py                   |       10 |        0 |    100% |           |
| mlrose\_ky/neural/activation/softmax.py                   |       11 |        0 |    100% |           |
| mlrose\_ky/neural/activation/tanh.py                      |       10 |        0 |    100% |           |
| mlrose\_ky/neural/fitness/\_\_init\_\_.py                 |        1 |        0 |    100% |           |
| mlrose\_ky/neural/fitness/network\_weights.py             |       80 |        9 |     89% |49, 53, 56, 59, 62, 65, 68, 71, 118 |
| mlrose\_ky/neural/linear\_regression.py                   |        6 |        0 |    100% |           |
| mlrose\_ky/neural/logistic\_regression.py                 |        6 |        0 |    100% |           |
| mlrose\_ky/neural/neural\_network.py                      |        6 |        0 |    100% |           |
| mlrose\_ky/neural/nn\_classifier.py                       |       74 |       65 |     12% |29-65, 68-73, 76, 80-134, 137-150, 153-154 |
| mlrose\_ky/neural/nn\_core.py                             |      134 |       20 |     85% |50, 80, 83, 86, 89, 92, 95, 98, 101, 103-106, 109, 112, 118, 159, 163, 192, 207, 292 |
| mlrose\_ky/neural/utils/\_\_init\_\_.py                   |        1 |        0 |    100% |           |
| mlrose\_ky/neural/utils/weights.py                        |       54 |        8 |     85% |54, 99, 102, 105, 109, 113, 143, 148 |
| mlrose\_ky/opt\_probs/\_\_init\_\_.py                     |        7 |        0 |    100% |           |
| mlrose\_ky/opt\_probs/continuous\_opt.py                  |       94 |       15 |     84% |41, 49, 52, 55, 101, 149, 151-154, 190, 193, 201-204, 235 |
| mlrose\_ky/opt\_probs/discrete\_opt.py                    |      201 |       65 |     68% |43, 51, 53-56, 108-113, 122-136, 148-208, 242, 261, 335, 337-340, 373, 376, 408, 410-413 |
| mlrose\_ky/opt\_probs/flip\_flop\_opt.py                  |       38 |       17 |     55% |18, 21, 38-39, 49-73, 76 |
| mlrose\_ky/opt\_probs/knapsack\_opt.py                    |       22 |        7 |     68% | 28, 31-36 |
| mlrose\_ky/opt\_probs/max\_k\_color\_opt.py               |       44 |        8 |     82% |22, 25-28, 47-49, 71 |
| mlrose\_ky/opt\_probs/opt\_prob.py                        |       79 |        6 |     92% |26, 28-31, 96, 237 |
| mlrose\_ky/opt\_probs/queens\_opt.py                      |       24 |        3 |     88% |18, 21, 40 |
| mlrose\_ky/opt\_probs/tsp\_opt.py                         |       80 |        9 |     89% |51, 59-60, 67, 142, 184, 186-189 |
| mlrose\_ky/runners/\_\_init\_\_.py                        |        7 |        0 |    100% |           |
| mlrose\_ky/runners/\_nn\_runner\_base.py                  |      150 |       28 |     81% |163, 179-181, 209-210, 217-218, 221-223, 290-291, 302, 312, 328-330, 347, 352-355, 380-382, 436-439 |
| mlrose\_ky/runners/\_runner\_base.py                      |      275 |      146 |     47% |101, 113, 145, 147, 149, 159, 287-289, 302-304, 316-321, 352-373, 388-393, 416-422, 437-440, 484-488, 499-519, 556-584, 590, 615-622, 663-746 |
| mlrose\_ky/runners/ga\_runner.py                          |       14 |        6 |     57% | 42-54, 57 |
| mlrose\_ky/runners/mimic\_runner.py                       |       20 |       11 |     45% |40-54, 57-59, 62 |
| mlrose\_ky/runners/nngs\_runner.py                        |       21 |       12 |     43% |64-92, 103-110 |
| mlrose\_ky/runners/rhc\_runner.py                         |       11 |        3 |     73% | 29-38, 41 |
| mlrose\_ky/runners/sa\_runner.py                          |       19 |       10 |     47% |45-60, 63-68 |
| mlrose\_ky/runners/skmlp\_runner.py                       |      101 |       80 |     21% |14-34, 37-39, 42-44, 47-51, 54-58, 61, 64-72, 75-80, 83-97, 130-169, 174-191 |
| mlrose\_ky/runners/utils.py                               |       14 |        2 |     86% |     37-38 |
| mlrose\_ky/samples/\_\_init\_\_.py                        |        1 |        0 |    100% |           |
| mlrose\_ky/samples/synthetic\_data.py                     |      122 |       28 |     77% |78-85, 168-188, 242, 256, 261-263, 272 |
| tests/\_\_init\_\_.py                                     |        0 |        0 |    100% |           |
| tests/test\_activation.py                                 |       50 |        4 |     92% |     10-14 |
| tests/test\_algorithms.py                                 |      114 |        4 |     96% |     10-14 |
| tests/test\_decay.py                                      |       38 |        4 |     89% |      8-12 |
| tests/test\_decorators.py                                 |       21 |        3 |     86% |22, 34, 44 |
| tests/test\_fitness.py                                    |       95 |        3 |     97% |     10-13 |
| tests/test\_generators.py                                 |      450 |        4 |     99% |      8-12 |
| tests/test\_gridsearch.py                                 |      114 |        7 |     94% |17-21, 60, 99, 165 |
| tests/test\_neural.py                                     |      262 |        3 |     99% |     11-14 |
| tests/test\_opt\_probs.py                                 |      339 |        4 |     99% |     10-14 |
| tests/test\_runners.py                                    |      238 |        5 |     98% |17-21, 103 |
| tests/test\_samples.py                                    |       45 |        4 |     91% |     14-18 |
|                                                 **TOTAL** | **4799** |  **865** | **82%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/nkapila6/mlrose-ky/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/nkapila6/mlrose-ky/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/nkapila6/mlrose-ky/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/nkapila6/mlrose-ky/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fnkapila6%2Fmlrose-ky%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/nkapila6/mlrose-ky/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.