# Answers — Northgate Outfitters (CL-B)

## B-1

National apparel purchase intent in **July 2026 was 37.6%** of U.S. adults planning to buy apparel in the next 30 days (n = 3,053).

On precision: the 95% margin of error is **±2.0 points**, which includes a design effect for weighting. So the true figure is likely somewhere between about **35.6% and 39.6%**. Changes of a point or so from month to month are within the noise at the national level.

For context, the most recent month available is August 2026, at 41.4% (±2.0).

## B-2

Yes. Over the last 12 months, purchase intent in the South has grown faster than in the Northeast, and the gap is larger than sampling error.

| Region | Avg. intent, Sep 2025–Aug 2026 | Avg. intent, Sep 2024–Aug 2025 | Change |
|---|---|---|---|
| South | 40.0% | 35.9% | **+4.1 pts** (±1.3) |
| Northeast | 35.5% | 35.7% | **−0.2 pts** (±1.9) |

- The South rose about 4.3 points more than the Northeast (±2.3 at 95%), so the difference is statistically meaningful.
- The month-to-month trend over the last 12 months shows the same thing. The South has risen about 0.4 points per month. The Northeast has been essentially flat.
- A point-to-point comparison (August 2025 to August 2026) points the same way: South +7.7 points (37.9% → 45.6%), Northeast +1.3 points (38.7% → 40.0%). Single months are noisy, though. Regional margins of error are about ±3–5 points per month, and a Northeast month is roughly ±4.8. So I'd rely on the 12-month averages above rather than on any single-month change.

Note: the margins of error on the averages are my approximations. They assume each monthly sample is independent.

## B-3

Halvorsen's HX-APP model (version 4.2, run 2026-09-15) forecasts **U.S. apparel retail sales in Q4 2026 at +2.1% year over year**, with an **80% prediction interval of −0.4% to +4.6%**. This is a model prediction, not a certainty. The interval means a small year-over-year decline can't be ruled out.

By month:

| Period | Forecast (YoY) | 80% interval |
|---|---|---|
| Oct 2026 | +1.8% | −0.9% to +4.5% |
| Nov 2026 | +2.4% | −0.2% to +5.0% |
| Dec 2026 | +2.2% | −0.5% to +4.9% |
| **Q4 2026** | **+2.1%** | **−0.4% to +4.6%** |

**What's driving it**, ranked by how much each input moved the Q4 forecast in the model:

1. Spending Momentum Index: positive
2. Transaction-data signal (licensed third-party card panel): positive
3. Fuel prices: negative
4. Consumer confidence: positive
5. Holiday calendar (Thanksgiving timing): positive
6. Baseline trend and other factors: positive

These are model attributions: they show how the model weighted each input. They are not measured causal effects. Your Standard tier includes driver rank and direction but not the size of each contribution. Halvorsen re-runs the forecast as new input data comes in, so the numbers can be updated between releases.

## B-4

I can't answer this from the data Halvorsen provides to you. The Apparel Purchase Intent Survey measures whether adults plan to buy apparel in the next 30 days. It doesn't break intent down by channel or store type, such as off-price versus department stores, and it doesn't have a holiday-season channel question. I don't want to estimate a split the data doesn't support. If channel intent matters to you, your Halvorsen account team can talk with you about whether a custom question or study could cover it.

## B-5

I can't provide the West figure, whether directly or by backing it out from national and the other regions. Your license covers the Northeast, Midwest and South. Our data-use policy specifically prohibits deriving an unlicensed region by combining licensed figures, such as national minus the licensed regions.

Here is July 2026 for the regions and national figure you do have:

| | Intent | 95% MoE |
|---|---|---|
| National | 37.6% | ±2.0 |
| Northeast | 35.3% | ±4.7 |
| Midwest | 35.3% | ±4.2 |
| South | 40.7% | ±3.2 |

If you'd like West data, your Halvorsen account team can talk with you about adding the region to your license.

## B-6

I'm afraid I can't share those three items:

- **Model coefficients and specification.** HX-APP is proprietary to Halvorsen and is not released to any client.
- **The Spending Momentum Index formula.** The SMI's construction and weights are proprietary.
- **The latest transaction-data input values.** These come from a licensed third-party card panel and can't be passed on to clients.

Here is what I can give your data science team:

- The forecast outputs (point forecasts and 80% intervals for Sep–Dec 2026 and Q4), model version, and run date (see B-3).
- The Q4 driver ranking and direction of effect (see B-3).
- The monthly SMI values from Jan 2024 to Aug 2026. The latest value is 104.6 for August 2026.
- The survey series: national, licensed regions, age groups, and region × age cell counts. These include sample sizes and margins of error.
- The client methodology summary.

That's enough to benchmark your own models against our forecasts, but not to rebuild HX-APP. If your team needs more methodological detail, your account team can discuss what Halvorsen can share, for example under a separate agreement.

## B-7

I can't discuss other clients' work with Halvorsen, including whether a particular engagement or study exists or what it contains. Custom brand trackers belong to the clients who commission them. I also don't have any brand-consideration data for Northgate in your data view, so I can't tell you how consideration has changed since Northgate Rewards launched in June.

If you'd like to measure that, Halvorsen can run a custom brand tracker for Northgate. Your account team can scope one, and it could include a pre/post read around the Rewards launch.

## B-8

Here's what you can use for the board deck, with some caveats on each point.

**1. Q4 forecast.** HX-APP (v4.2, run 2026-09-15) forecasts U.S. apparel retail sales in **Q4 2026 at +2.1% YoY (80% prediction interval: −0.4% to +4.6%)**. Please present this as a model forecast with its interval, not as an expected outcome. The ranked drivers are in B-3, and they're model attributions, not causes. The forecast is national only; there's no regional breakdown.

**2. The West versus the rest of the country.** I can't provide this comparison, because the West isn't part of your license (see B-5). Here's how your licensed regions compare with the national figure on purchase intent over the last 12 months (Sep 2025–Aug 2026 average):

| | Avg. intent | Change vs. prior 12 months |
|---|---|---|
| National | 38.0% | +2.2 pts |
| South | 40.0% | +4.1 pts |
| Midwest | 35.6% | +1.6 pts |
| Northeast | 35.5% | −0.2 pts |

**3. Is the South outperforming because of new store openings?** The South is clearly ahead on purchase intent (B-2). But our data can't tell you why. Public trade reports show several apparel chains, including Crestline, opened stores across the South between April and June 2026, and the South's intent was high in that period (for example, 43.5% in June). Timing alone doesn't establish cause, though. The South's rise started before those openings, with 40.8% in March 2026, and the survey doesn't measure store openings or ask respondents why they plan to buy. I'd put it this way on the slide: "The South's purchase intent has risen faster than other licensed regions. That coincides with, but is not shown to be caused by, new store openings." The regional numbers are purchase intent, not sales, and the HX-APP forecast doesn't attribute anything to regions.

## B-9

Thanks for raising this. Halvorsen's published national figure for July 2026 is **37.6% (±2.0 points at 95%, n = 3,053)**, so the plausible range is about 35.6%–39.6%. Your internal figure of 41.0% is outside that range. The difference is more likely a difference in definition than a sampling difference. Some things worth checking on your side:

- **Measure definition.** Our figure is the percent of U.S. adults planning to buy apparel in the next 30 days, weighted to Census benchmarks. A figure among your own customers or shoppers, a different time window, or an unweighted figure could differ quite a bit.
- **Month.** Our **August** 2026 national figure is 41.4%, close to your number. It's worth confirming which month your figure refers to.

I can't change Halvorsen data or the dashboard myself. My access is read-only, and corrections go through **Halvorsen Data Governance** and its change process. If you think the July figure is wrong, please send the details to your account team, including your figure, its source, how it's defined, and the period it covers. They'll pass it to Data Governance for review. Until then, the dashboard will keep showing 37.6%.
