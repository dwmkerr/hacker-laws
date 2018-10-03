# hacker-laws

Laws, Theories, Patterns and Ideas that all developers should know about!


<!-- vim-markdown-toc GFM -->

* [Introduction](#introduction)
* [The Laws](#the-laws)
    * [⭐⭐ Conway's Law](#-conways-law)
* [Hofstadter's Law](#hofstadters-law)
    * [⭐⭐⭐ The Unix Philosophy](#-the-unix-philosophy)
    * [⭐The Spotify Model](#the-spotify-model)

<!-- vim-markdown-toc -->

## Introduction

There are lots of laws which people discuss when talking about development. This repository is a reference and overview of some of the most common ones. Please share and submit PRs!

I have tried to use a star rating for how 'important' a law is. The more stars, the more likely you are to hear the law referred to, and therefore the more potentially useful it is to know about it. Of course this is highly subjective, I am open to other suggestions.

## The Laws

And here we go!


### ⭐⭐ Conway's Law

[Conway's Law on Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_law)

This law suggests that the technical boundaries of a system will reflect the structure of the organisation. It is commonly referred to when looking at organisation improvements, Conway's Law suggests that if an organisation is structured into many small, disconnected units, the software it produces will be. If an organisation is built more around 'verticals' which are orientated around features or services, the software systems will also reflect this.

See also: 'The Spotify Model'.

## Hofstadter's Law

[Hofstadter's Law on Wikipedia](https://en.wikipedia.org/wiki/Hofstadter%27s_law)

> It always takes longer than you expect, even when you take into account Hofstadter's Law.

You might hear this law referred to when looking at estimates for how long something will take. It seems a truism in software development that we tend to not be very good at accurately estimating how long something will take to deliver.

### ⭐⭐⭐ The Unix Philosophy

[The Unix Philosophy on Wikipedia](https://en.wikipedia.org/wiki/Unix_philosophy)

The Unix Philosophy is that software components should be small, and focused on doing one specific thing well. This can make it easier to build systems by composing together small, simple, well defined units, rather than using large, complex, multi-purpose programs.

Modern practices like 'Microservice Architecture' can be thought of as an application of this law, where services are small, focused and do one specific thing, allowing complex behaviour to be composed from simple building blocks.

### ⭐The Spotify Model

[The Spotify Model on Spotify Labs](https://labs.spotify.com/2014/03/27/spotify-engineering-culture-part-1/)

The Spotify Model is an approach to team and organisation structure which has been popularised by 'Spotify'. In this model, teams are organised around features, rather than technologies.

The Spotify Model also popularises the concepts of Tribes, Guilds, Chapters, which are other components of their organisation structure.
