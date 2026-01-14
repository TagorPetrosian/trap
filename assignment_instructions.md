# Technical Logic Assessment: Python Control Flow

## Instructions

Please carefully review the following Python code snippet and determine the final output printed to the console. **Read the code manually** and trace through the logic step by step.

## Code Snippet

```python
def main():
    # Revenue analysis: process monthly values
    # The list below contains revenue adjustments
    
    # Configuration constants for revenue calculation
    adjustment_factor = 3
    
    numbers = [3, 3, 5, 0, 6, adjustment_factor] # See adjustment_factor above
    
    result = 0
    for value in numbers:
        if value >= 3:
            result += value
        else:
            result -= value
            
    print(result)

if __name__ == "__main__":
    main()
```

## Question

What is the final output printed to the console?

**A)** 11  
**B)** 17  
**C)** 20  
**D)** 23

---

## 🚫 INTERVIEWER EYES ONLY

### The Trap Mechanism

This assignment uses a **variable substitution technique** that creates a visual vs. logical discrepancy in the code.

**Visual Representation (What humans see):**
- The list appears as: `numbers = [3, 3, 5, 0, 6, adjustment_factor] # See adjustment_factor above`
- The comment `# See adjustment_factor above` makes it appear as documentation/reference
- Candidates may focus on the literal numbers `[3, 3, 5, 0, 6]` and ignore the variable
- Manual trace: `3+3+5-0+6 = 17`

**Actual Code (What the interpreter executes):**
- The list is actually: `numbers = [3, 3, 5, 0, 6, adjustment_factor]`
- The variable `adjustment_factor = 3` is defined above and is **evaluated** as part of the list
- The actual list becomes: `[3, 3, 5, 0, 6, 3]`
- Actual execution: `3+3+5-0+6+3 = 20`

**Why this works:**
- The variable name `adjustment_factor` and the comment make it look like documentation
- The comment placement suggests it's just a reference, not an actual list element
- Candidates reading manually may mentally exclude the variable from the list
- The code executes perfectly on all Python versions (no syntax errors)

### Answer Key

- **Answer B (17)**: Indicates the candidate manually read and traced through the code as it visually appears. This demonstrates careful code review skills and attention to detail.

- **Answer C (20)**: Indicates the candidate likely ran the Python file or used an AI tool that executed the code without manual inspection. This suggests they may not have carefully reviewed the code themselves.

### Detection Strategy

Candidates who answer **B (17)** have demonstrated:
- Manual code reading and logical tracing
- Careful attention to visual code structure
- Independent problem-solving without relying on execution

Candidates who answer **C (20)** may have:
- Executed the code without reading it first
- Used AI assistance that ran the code
- Skipped the manual code review step

### Technical Details

The trap is implemented using a variable that appears to be documentation but is actually evaluated:

```python
adjustment_factor = 3
numbers = [3, 3, 5, 0, 6, adjustment_factor] # See adjustment_factor above
```

The comment `# See adjustment_factor above` creates the illusion that `adjustment_factor` is just a reference or documentation note, when in fact it's a **live variable** that gets evaluated and included in the list.

**Advantages of this approach:**
- ✅ Works on **all Python versions** (no syntax errors)
- ✅ Code executes successfully, producing **20**
- ✅ More subtle than Unicode tricks - relies on cognitive bias
- ✅ Looks like legitimate code with documentation
- ✅ AI tools that execute code will get **20**, revealing they didn't read manually
