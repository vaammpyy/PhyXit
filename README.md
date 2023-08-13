# PhyXit
![logo](./figures/logo.jpg)
1) Bot intro 
2) invite link
3) description

Introducing PhyXit: Your Ultimate Physics Companion

Step into the world of physics with PhyXit, your virtual assistant for all things related to the fundamental laws that govern our universe. Whether you're a student, researcher, or simply curious about the mysteries of the physical world, PhyXit is here to make your journey through physics smoother and more enjoyable.

PhyXit is more than just a bot; it's your personal simulator, research navigator, and professor contact hub all rolled into one. Here's what PhyXit can do for you:

Simulation Made Simple: Unveil the secrets of basic physical systems through interactive simulations. Whether you're exploring the motion of objects, understanding the behavior of waves, or experimenting with simple pendulums, PhyXit's simulations provide an immersive way to grasp complex concepts.

Research at Your Fingertips: Dive into the vast sea of physics research effortlessly. PhyXit can fetch research papers and summaries from arXiv, ensuring you're always up-to-date with the latest advancements. Whether you're studying quantum mechanics or cosmic phenomena, PhyXit makes accessing knowledge a breeze.

Connect with Professors: Need guidance or assistance? PhyXit has got you covered. Discover contact details and information about professors in the field of physics. Whether you're seeking to discuss research opportunities, ask questions about theories, or explore potential collaborations, PhyXit can help you connect.

Get ready to embark on a journey through the wonders of physics with PhyXit as your trusty companion. Empower your learning, research, and connections in the world of physics like never before. Let PhyXit be your bridge to understanding the universe's most intriguing phenomena.


# Simulation quick start guide

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
*   Charge Interaction: `charge`

`@PhyXit sim <sim-name> *<initial-conditions>`

For details regarding the initial conditions of the simulations use.

`@PhyXit sim -h`

## Arxiv and Wikipedia

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

# How you can contribute?

All our solver codes are present in the 

