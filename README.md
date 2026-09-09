# genpark-shannon-entropy-mutual-information-estimator-skill

[![GitHub stars](https://img.shields.io/github/stars/Alpha-Park/genpark-shannon-entropy-mutual-information-estimator-skill?style=social)](https://github.com/Alpha-Park/genpark-shannon-entropy-mutual-information-estimator-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0%20external-brightgreen.svg)](#)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20Compatible-orange.svg)](#)

> Autonomous Agent Shannon Entropy, Mutual Information, Kullback-Leibler Divergence & Jensen-Shannon Estimator

Part of the **GenPark Autonomous Information Theory & Optimal Entropy Coding Swarm**.

## Architecture Overview

```mermaid
graph TD
    A[Probability Distribution / Joint Matrix] --> B[Shannon Entropy H X]
    A --> C[Conditional Entropy H X|Y]
    A --> D[Mutual Information I X;Y]
    A --> E[Kullback-Leibler Divergence D_KL P||Q]
    E --> F[Symmetric Jensen-Shannon Divergence JSD]
    B --> G[Information Gain & Feature Selection]
    D --> G
    F --> H[Semantic Drift & Anomaly Detection]
```

## Features

- **Pure Python Standard Library**: Zero external dependencies. Runs anywhere.
- **Production-Grade Design**: Type annotations, exhaustive edge cases, robust numerical stability.
- **MCP Server Ready**: Built-in stdio Model Context Protocol (MCP) server for Claude / Cursor / Agent tool calling.
- **Benchmark Validated**: 100% verified test coverage in isolated sandbox environments.

## Quickstart

```bash
git clone https://github.com/Alpha-Park/genpark-shannon-entropy-mutual-information-estimator-skill.git
cd genpark-shannon-entropy-mutual-information-estimator-skill
python example_usage.py
```

## Model Context Protocol (MCP) Usage

```bash
python mcp_server.py
```

## License

MIT License. Designed for autonomous agentic workflows.
