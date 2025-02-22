
<div class="h3-box" markdown="1">

## Dyslexia Word Swap

This test assesses the NLP model's capability to handle input text with common word swap errors associated with dyslexia. A Dyslexia Word Swap dictionary is employed to apply the most common word swap errors found in dyslexic writing to the input data.

**alias_name:** `dyslexia_word_swap`

<i class="fa fa-info-circle"></i>
<em>To test QA models, we are using QAEval from Langchain where we need to use the model itself or other ML model for evaluation, which can make mistakes.</em>

</div><div class="h3-box" markdown="1">

#### Config
```yaml
dyslexia_word_swap:
    min_pass_rate: 0.7
```
- **min_pass_rate (float):** Minimum pass rate to pass the test.

</div><div class="h3-box" markdown="1">

#### Examples

{:.table2}
|Original|Test Case|
|-|
|Please, you should be careful and must wear a mask.|Please, you should be careful and must where a mask.|
|Biden hails your relationship with Australia just days after new partnership drew ire from France.|Biden hails you're relationship with Australia just days after new partnership drew ire from France.|

</div>