---
title: "Latex"
tags:
  - plugin/transformer
---

This plugin adds LaTeX support to Quartz. See [[features/Latex|Latex]] for more information.

> [!note]
> For information on how to add, remove or configure plugins, see the [[configuration#Plugins|Configuration]] page.

This plugin accepts the following configuration options:

- `renderEngine`: the engine to use to render LaTeX equations. Can be `"katex"` for [[KaTeX]], `"mathjax"` for [[MathJax]] [[SVG rendering]], or `"typst"` for [[Typst]] (a new way to compose LaTeX equation). Defaults to KaTeX.
- `customMacros`: custom macros for all LaTeX blocks. It takes the form of a key-value pair where the key is a new command name and the value is the expansion of the macro. For example: `{"\\R": "\\mathbb{R}"}`

> [!note] Typst support
>
> Currently, typst doesn't support inline-math

## API

- Category: Transformer
- Function name: `Plugin.Latex()`.
- Source: [[`quartz/plugins/transformers/latex.ts`]].
