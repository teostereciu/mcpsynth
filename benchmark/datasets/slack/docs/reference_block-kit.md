# Reference: Block Kit

*Source: https://docs.slack.dev/reference/block-kit*

---

[Block Kit](/block-kit) is made up of many atomic building blocks.

**Blocks** are visual components that can be arranged to create app layouts. Apps can add blocks to _surfaces_ like [App Home](/surfaces/app-home), [messages](/messaging) and [modals](/surfaces/modals).

Blocks may also contain **block elements**. Block elements are usually interactive components, such as buttons and menus.

Blocks and block elements are built with **composition objects**. Composition objects define text, options, or other interactive features within certain blocks and block elements.

* * *

## Tips for building with Block Kit​

### Use a framework​

Slack offers the Bolt framework in [Python](/tools/bolt-python/), [JavaScript](https://docs.slack.dev/tools/bolt-js), and [Java](/tools/java-slack-sdk/guides/bolt-basics/). Using the Bolt framework simplifies a lot of app building and abstracts the minutia to the framework to handle. When using Bolt, however, the format of blocks is slightly different than JSON. Each [block](/reference/block-kit/blocks) example shows the block used in each framework, but don't forget to add the imports! Clicking the link on each example takes you to the code in GitHub, where you can verify which libraries are needed.

### Remember to nest elements and composition objects​

Block Kit elements and composition objects are smaller units within another block. Each Block Kit element reference page includes a "Works with Blocks" reference and example of how to use it within that block. Composition object reference pages also include which block they can be used within.

### Test it out​

Test how your blocks will appear in [Block Kit Builder](https://app.slack.com/block-kit-builder).

* * *

## Blocks​

All

Name

Description

Surfaces

* * *

## Block elements​

All

All

Name

Description

Blocks

Surfaces

* * *

## Composition objects​

Name

Description

* * *