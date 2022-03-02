def arithmetic_arranger(questions, answer=False):
  
    if len(questions) > 5:
        return "Error:The questions should not exceed five."
    
    operator, op1, op2 = []
   

    for question in questions:
        pieces = problem.split()
       op1.append(pieces[0])
        operator.append(pieces[1])
        op2.append(pieces[2])

    # Checking for * or / operators
    if "/" in operator or "*" in operator:
        return "Error: Operator must be '+' or '-' only."
    
     # Checking length
    for i in range(len(op1)):
        if len(op1[i]) > 4 or len(second_operand[i]) > 4:
            return "Error: Numbers cannot exceed four digits."

    # Checking digits
    for i in range(len(op1)):
        if not (op1[i].isdigit() and op2[i].isdigit()):
            return "Error: Digits only !!."

   

  line1,  line2,  line3,  line4 = []
    

    for i in range(len(op1))
        if len(op1[i]) > len(op2[i]):
            line1.append(" "*2 + op1[i])
        else:
         line1.append(" "*(len(op2[i]) - len(op1[i]) + 2) + op1[i])

    for i in range(len(op2)):
        if len(op2[i]) > len(op1[i]):
            line2.append(operator[i] + " " + op2[i])
        else:
           line2.append(operator[i] + " "*(len(op1[i]) - len(op2[i]) + 1) + op2[i])

    for i in range(len(op1)):
       line3.append("-"*(max(len(op1[i]), len(op2[i])) + 2))

    if answer:
        for i in range(len(op1)):
            if operator[i] == "+":
                ans = str(int(op1[i]) + int(op2[i]))
            else:
                ans = str(int(op1[i]) - int(op2[i]))

            if len(ans) > max(len(op1[i]), len(op2[i])):
               line4.append(" " + ans)
            else:
                line4.append(" "*(max(len(op1[i]), len(op2[i])) - len(ans) + 2) + ans)
        arranged_questions = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3) + "\n" + "    ".join(line4)
    else:
        arranged_questions = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3)
    return arranged_questions
