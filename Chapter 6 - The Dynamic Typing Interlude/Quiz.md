# Quiz Chapter 05

**1. Consider the following three statements. Do they change the value printed for A?**
    `A = "spam"`
    `B = A`
    `B = "shrubbery"`

    No, A still prints as "spam".

**2. Consider these three statements. Do they change the printed value of A?**
    `A = ["spam"]`
    `B = A`
    `B[0] = "shrubbery"`

    Yes A now prints as ["shrubbery"].

**3. How about these—is A changed now?**
    `A = ["spam"]`
    `B = A[:]`
    `B[0] = "shrubbery"`

    No, A still prints as ["spam"].
