# Day 2 Assignment – Reasoning and Acting

## 1. Scenario

For this assignment, I selected a college annual event budget comparison scenario.

A college wants to compare two event packages. Package A costs ₹20,000 and Package B costs ₹25,000. A 10% discount is applied to both packages. The task is to determine which package is cheaper after the discount and calculate the difference between the final prices.

The scenario was implemented using three approaches: Direct Prompting, Chain-of-Thought prompting, and a ReAct agent. A self-consistency experiment was also performed to observe how repeated runs behave at a non-zero temperature.

The final discounted prices are ₹18,000 for Package A and ₹22,500 for Package B. Therefore, Package A is cheaper by ₹4,500.

---

# 2. Explanation of Each Approach

## 2.1 Direct Prompting

Direct prompting sends the user's question directly to the language model and asks it to provide an answer. The model responds immediately without exposing a reasoning process and without calling any external tools.

In this scenario, the direct-prompting program was intentionally not given access to the external package-pricing information. Therefore, it could not retrieve missing package prices from an external source. This demonstrates an important limitation of direct prompting: the model can work with information supplied in the prompt or information already available to it, but it cannot independently fetch missing information without a tool.

The flow of direct prompting is simple:

User Question → Language Model → Final Answer

Direct prompting is therefore suitable for simple questions where all required information is already available in the prompt.

---

## 2.2 Chain-of-Thought Prompting

Chain-of-Thought prompting asks the model to work through a problem step by step before producing its final answer. It is useful when a question requires several connected calculations or reasoning steps.

For this scenario, the package prices were explicitly provided to the model. It could therefore calculate the 10% discount for each package and compare the resulting prices without needing an external tool.

The calculation was:

Package A = ₹20,000

10% discount = ₹2,000

Final price of Package A = ₹18,000

Package B = ₹25,000

10% discount = ₹2,500

Final price of Package B = ₹22,500

Difference = ₹22,500 − ₹18,000 = ₹4,500

Chain-of-Thought therefore helped the model handle the multi-step calculation. However, it still did not provide external information. If the package prices were unknown and required from an external pricing system, Chain-of-Thought alone would not be sufficient.

The flow is:

User Question → Step-by-Step Reasoning → Final Answer

---

## 2.3 ReAct Agent

ReAct stands for Reasoning and Acting. It combines reasoning with tool usage. Instead of answering immediately, the agent determines what information it needs, calls an appropriate tool, observes the result, and then continues until it can produce a final answer.

For this scenario, two tools were provided:

1. `get_package_price()` – obtains the price of an event package.
2. `calculator()` – performs mathematical calculations.

The ReAct process used the package-price tool to obtain the prices of Package A and Package B. It then used the calculator to apply the 10% discount and compare the final prices.

The general ReAct cycle is:

Question → Thought → Action → Observation → Thought → Action → Observation → Final Answer

The ReAct agent therefore demonstrated the ability to combine reasoning with external tool results. Unlike direct prompting and Chain-of-Thought, it did not need all the required information to be included directly in the user question.

One limitation is that ReAct requires additional tool calls and therefore involves more steps than a simple direct response.

---

# 3. Comparison Table

| Basis for comparison | Direct prompting | Chain-of-Thought | ReAct agent |
|---|---|---|---|
| Reasoning depth | Low; gives a direct response without a visible reasoning process. | Higher; works through multiple reasoning steps before answering. | Higher; combines reasoning with actions and observations from tools. |
| Tool usage | No tool usage. | No tool usage in this experiment. | Uses tools such as package-price lookup and calculator. |
| Reliability on multi-step questions | Can work for simple questions but may struggle when several calculations are required. | Better suited to multi-step calculations when the required information is already available. | Suitable for multi-step tasks that also require external information and calculations. |
| Transparency | The answer is provided directly without visible reasoning. | The prompt asks the model to reason step by step, but the reasoning process is not treated as a tool trace. | Tool actions and observations can be displayed, making the interaction with tools easier to follow. |
| Speed / cost | Usually fastest because there are no tool calls. | May require more reasoning tokens than direct prompting. | Usually involves additional tool calls and therefore can take more time and resources. |
| Consistency across repeated runs | Can vary depending on model settings and temperature. | Can vary at non-zero temperature. | Can vary because both model decisions and tool-use sequences can vary. |

---

# 4. Self-Consistency Observation

Self-consistency was tested using the same package-discount reasoning problem. The model was run five times at a temperature of 0.8.

The five observed answers were:

- Run 1: Package A; Difference: 4500
- Run 2: Package A; Difference: 4500
- Run 3: Package A; Difference: 4500
- Run 4: Package A; Difference: 4500
- Run 5: Package A; Difference: 4500

The majority answer was:

**Package A; Difference: 4500**

It received 5 out of 5 votes. The majority answer was correct because Package A has a final price of ₹18,000, while Package B has a final price of ₹22,500, giving a difference of ₹4,500.

When the temperature was changed to 0, the program was run again to observe the effect of deterministic generation. The temperature-0 result should be reported according to the actual terminal output from that run.

The experiment shows that repeated sampling can be used to observe whether a model produces the same answer consistently. In this particular experiment, all five runs at temperature 0.8 produced the same final answer.

---

# 5. Suitability Analysis

For the selected college event budget scenario, the three approaches demonstrate different capabilities.

Direct prompting is suitable when the required information is already available and the problem is simple. It has a straightforward interaction because the model produces an answer without using tools.

Chain-of-Thought prompting is useful when the problem requires several reasoning or calculation steps. In this experiment, the model could calculate the discounted prices because the package prices were supplied directly in the question. However, Chain-of-Thought does not itself provide a mechanism for retrieving missing external information.

The ReAct approach is useful when a problem requires both reasoning and external information. In this scenario, the ReAct agent used `get_package_price()` to obtain package prices and `calculator()` to perform the calculations. This demonstrates the main advantage of ReAct for tasks that combine information retrieval with reasoning and action.

The self-consistency experiment produced the same correct answer in all five runs at temperature 0.8. This provided an additional observation about consistency for the selected reasoning question.

---

# 6. Conclusion

Direct prompting, Chain-of-Thought prompting, and ReAct are useful for different types of problems.

Direct prompting is appropriate for straightforward questions where the required information is already available and no external tools are required.

Chain-of-Thought prompting is useful for problems that require multiple reasoning or calculation steps. It can help organize the solution process, but it does not by itself provide access to external information.

ReAct is appropriate for problems where the model needs to reason while interacting with tools or external information. It follows a cycle of reasoning, action, and observation before producing a final answer.

Therefore, the main difference between the three approaches is not simply the amount of reasoning. It is also whether the system can interact with external tools. Direct prompting answers directly, Chain-of-Thought focuses on multi-step reasoning using the available information, and ReAct combines reasoning with tool interaction.