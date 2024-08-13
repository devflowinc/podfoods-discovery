<p align="center">
  <img height="100" src="https://cdn.trieve.ai/trieve-logo.png?" alt="Trieve Logo">
</p>
<p align="center">
<strong><a href="https://dashboard.trieve.ai">Sign Up (1k chunks free)</a> | <a href="https://docs.trieve.ai">Documentation</a> | <a href="https://cal.com/nick.k/meet">Meet With a Founder</a> | <a href="https://discord.gg/eBJXXZDB8z">Discord</a> | <a href="https://matrix.to/#/#trieve-general:trieve.ai">Matrix</a>
</strong>
</p>

<p align="center">
    <a href="https://github.com/devflowinc/trieve/stargazers">
        <img src="https://img.shields.io/github/stars/devflowinc/trieve.svg?style=flat&color=yellow" alt="Github stars"/>
    </a>
    <a href="https://github.com/devflowinc/trieve/issues">
        <img src="https://img.shields.io/github/issues/devflowinc/trieve.svg?style=flat&color=success" alt="GitHub issues"/>
    </a>
    <a href="https://discord.gg/CuJVfgZf54">
        <img src="https://img.shields.io/discord/1130153053056684123.svg?label=Discord&logo=Discord&colorB=7289da&style=flat" alt="Join Discord"/>
    </a>
    <a href="https://matrix.to/#/#trieve-general:trieve.ai">
        <img src="https://img.shields.io/badge/matrix-join-purple?style=flat&logo=matrix&logocolor=white" alt="Join Matrix"/>
    </a>
</p>

<h2 align="center">
    <b>Trieve Pod Foods Discovery Project</b>
</h2>

![Screenshot of a search for [Texas boutique tea yerba] on podfoods.trieve.ai](https://cdn.trieve.ai/github/trieve-podfoods-demo-screenshot.webp?)

Preview the output of this project at [podfoods.trieve.ai](https://podfoods.trieve.ai)

## About

Pod Foods co-founders, Fiona Lee and Larissa Russell decided to build their company after experiencing distribution challenges with their first business selling cookies.

Pod Foods is currently disrupting grocery distribution with their marketplace enabling retailers and emerging brands to connect.

### Search For More Bespoke, Health-Oriented, and New Products is a Fun Challenge

Keyword search is enough for the vast majority of queries when someone knows what they're looking for, but less so when you're exploring. Pod Foods is really interesting because they are likely to have a significant number of users **exploring** more-so than checking if a specific item is present.

Trieve provides vector based search for semantic, fulltext, and hybrid modes which is uniquely well-suited to Pod Foods' dataset.

### Areas We Tried To Improve

## How To Contribute

Setup your local dev environment following the guide in the next section, fork the repo, and post a PR with your changes!

If you are doing something more significant and want to get a hold of us beforehand then send an email to [humans@trieve.ai](mailto:humans@trieve.ai) or ping us on our Matrix or Discord linked in the badges at the top of this README.

## How To Setup Local Dev

### Environment Variables

`.env.dist` in the root folder contains a read-only API Key and dataset-ID. These env's will work out of the box for the `frontend`. However, if you want to run the crawker, you will need to get an API Key with write permissions. Reach out to us at <humans@trieve.ai> or follow our [quickstart guide](https://docs.trieve.ai/getting-started/quickstart) to create a new dataset.

Run the following to setup env's for the frontned:

```
cp .env.dist ./frontend/.env
```

### Run Frontend Locally

Frontend of this application

```
cd frontend
yarn
yarn dev
```

### Run the Crawler

<!-- TODO: Include Bit for Creating a new Dataset and Changing ENV's; Fine to link out to docs for this -->
