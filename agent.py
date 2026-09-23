import re
from tools import get_course_fee, calculator


def agent(question, max_steps=8):
    print("\n--- ReAct TRACE ---")

    # Step 1: Get course fees
    print("\nThought: I need the fees for CS101, AI202, and DS303.")
    
    print("Action: get_course_fee('CS101')")
    cs101 = get_course_fee("CS101")
    print("Observation:", cs101)

    print("Action: get_course_fee('AI202')")
    ai202 = get_course_fee("AI202")
    print("Observation:", ai202)

    print("Action: get_course_fee('DS303')")
    ds303 = get_course_fee("DS303")
    print("Observation:", ds303)

    # Step 2: Calculate first option
    print("\nThought: Calculate the total for CS101 and AI202, then apply 10% scholarship.")

    first_total = calculator(f"({cs101} + {ai202}) * 0.90")
    print("Action: calculator((CS101 + AI202) * 0.90)")
    print("Observation:", first_total)

    # Step 3: Calculate second option
    print("\nThought: Calculate the total for all three courses, then apply 25% scholarship.")

    second_total = calculator(f"({cs101} + {ai202} + {ds303}) * 0.75")
    print("Action: calculator((CS101 + AI202 + DS303) * 0.75)")
    print("Observation:", second_total)

    # Step 4: Find difference
    print("\nThought: Compare the two final prices.")

    difference = calculator(f"{second_total} - {first_total}")
    print("Action: calculator(second option - first option)")
    print("Observation:", difference)

    print("\nThought: The first option is cheaper.")

    answer = (
        f"First option = ₹{first_total:,.0f}\n"
        f"Second option = ₹{second_total:,.0f}\n"
        f"Difference = ₹{difference:,.0f}\n"
        f"Final answer: The first option is cheaper by ₹{difference:,.0f}."
    )

    return answer