## Bot is not currently hosted, we are not maintaining the project in the near future.
# PhyXit
![logo](./figures/logo.jpg)

Meet **PhyXit**: The Discord bot for physics enthusiasts. Simulate physical systems, fetch ArXiv papers, summarize wikipedia articles and get professor's google scholar profile with ease. [Invite](https://discord.com/api/oauth2/authorize?client_id=1139830899685474395&permissions=108544&scope=bot%20applications.commands) PhyXit to your discord server and elevate your physics discussions and research endeavors today! 


# Simulation quick start guide

**NOTE**: Tag PhyXit explicitly in the discord server to give commands.

* To run a quick simulation use the following commands:
    1) Projectile : `@PhyXit sim projectile 10 45 5 0.1 5` 
    2) Simple pendulum : `@PhyXit sim pendulum 1 1 45 0 0.5 0.1 5`
    3) Spring and mass system: `@PhyXit sim spring 1 10 1 1.5 0 0.3 0.1 5`
    4) Diffusion: `@PhyXit sim diffusion 30 50 0.1`
    5) Charge particle interaction: `@PhyXit sim charged_int 2 -1 2 1 -1 0 1 0 0 0.1 5`

# Usage

## Simulations

You can use PhyXit currently to run the following simulations:-
*   Projectile motion: `projectile`
*   Simple pendulum: `pendulum`
*   Spring mass: `spring`
*   Diffusion: `diffusion`
*   Charge Interaction: `charged_int`

`@PhyXit sim <sim-name> *<initial-conditions>`

For details regarding the initial conditions of the simulations use.

`@PhyXit sim -h`

## ArXiv and Wikipedia

PhyXit can also fetch results from [arxiv](https://arxiv.org/) and [wikipedia](https://www.wikipedia.org/).

* To get 10 latest research papers related to a certain keyword you can use.

`@PhyXit arxiv top <keywords>`

* If you know the arxiv `paper-id` you can directly get a summary of it and a downloadable pdf using PhyXit.

`@PhyXit arxiv fetch <paper-id>`

* Phyxit can also summarize [wikipedia](https://www.wikipedia.org/) articles for you.

`@PhyXit arxiv wiki <search-query>`

## Google Scholar

PhyXit can also display a professor's google scholar profile.

`@PhyXit profs name <Name>`
