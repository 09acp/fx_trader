# FX Trader - GAF classifier - Raw usd/eur prices
Alex Papa 03/02/2020
"
The aim is to use the thesis stock trading project as a template for FX trading. The model will only use GAF features based on price data (most successful), to determined the daily price movement (Buy/Sell).

The second goal is to test the hypothesis that by visualising the prediction of the model, a trader can divide the total trades executed by subgroup according to the conviction of the model and PCs. Ideally, trading a specific subgroup will be more profitable that trading all forecasted positions, because it will minimize false positives and false negatives.

The final goal is to test the hypothesis that by visually evaluating the time-series of a potential trade (chosen subgroup), the trader can determine whether to go through with the trade or not, hence adding human expertise into the trading system. This evaluation will be executed through a slick Dash browser app.
"
#### __Project Summary__
- [ ] [one_pager](link)

#### __Data Processing__
_FX_data folder_ - Script generates input data for modelling
- [x] [data_generator](link)
  - [x] Use a single currency pair USD/EUR from [Investing.com](https://www.investing.com/currencies/eur-usd-historical-data)
  - [x] download 4 x 10yr csvs (limit on draw) - remove duplicates
  - [x] create train / test sets 80-20
  - [x] create labels **(Buy/Sell)** for supervised learning (5d window, 1 step)
  - [x] create GADF tensor
  - [x] save as pickle "usd_eur_gadf.pkl"
~~_Toolbox_ - Script with helper functions
- [ ] [toolbox](link)~~

#### __ML Classifiers__
Non-ANN classifiers
- [x] [ml_classifiers](link)  # scirpt
  - [x] **Flatten ndarrays into 2d tensors for use by models** (Important)
  - [x] Logistic Regression
  - [ ] ~~Random Forest~~
  - [x] [Recursive Feature Elimination - Images](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_digits.html#sphx-glr-auto-examples-feature-selection-plot-rfe-digits-py)
  - [ ] TF2 Logistic Regression
  - [x] gather all features into single df and save to database

#### __Trading Experiment__
Trading agent backtest on model forecasts
- [x] [trader](link)  # scirpt
  - [x] create single df with forecasts and __raw features__
  - [x] create trading log
  - [x] plot results & save to databse

#### __Prep data for Viz__
- [x] [eda_data_prep](link)
  - [x] MinMax scale independent features (continuous)
  - [x] apply PCA on independent vars
  - [x] K-means with 10 clusters to create subgroups on PCA outputs
  - [x] Reduce dimensions / clustering using t-SNE
  - [x] Save data to database: _"eda_data_LR"_
  - [x] Plot draft 3D scatterplot of 2PCS Vs profit
  - [x] Plot draft 3D scatterplot of 2tSNE Vs profit

#### __Trader Visual Evaluation (local)__
- [x] [eda_local](link)
  _Evaluate visualisation of subgroups - determine most interpretable method_
  - [x] PCA subgroups
  - [x] t-SNE subgroups
  - [ ] Add [surface](https://plot.ly/python/3d-surface-plots/) plane to the 3d plot (mean profitability)

  _H1: In depth analysis of trade subgroups_
  Analyse trades according to various metrics
  - [x] Visual analysis of profitable trades
  - [x] Visual analysis of trades chronologically
  - [x] Statistical analysis of subgroup profitability
  - Save to Database _"profitable_subgroups"_ . subgroup_trades.txt

#### __Trading Dashboard (app)__
Human-Model trading on trade subgroups - H2
- [x] [eda_dash](link)
  - [x] 3D scatter plot for subgroups
  - [x] date range picker - year
  - [x] cluster groups dropdown
  - [x] action checklist  (FIX NAMES ) -->> DROPDOWN INSTEAD
  - [ ] correctly predicted checklist
  - [x] ~~only-profitable subgroup checklist~~
        dataset selection dropdown (all_trades / subgroups)

  - [ ] Subplot -> Price Series
  - [ ] Subplot -> Cluster group stats
  - [ ] Subplot -> pca results?




  _H2: Human-Model trading profitability_
  - [ ]

  _H3: Test subgroup profitability on unseen data_


#### __APP ???__
- [ ] [script](link)
  - [ ] Step 1
  - [ ] Step 2

**link images** from image folder


#### Additional Ideas
- Use unseen data (post 2010) to see whether the profitability of subgroups holds up.
  - ...