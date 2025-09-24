This repository tracks my journey of learning **DSA, Python, and projects** step by step.  
Goal: Build problem-solving skills, Python proficiency, and maintain a professional portfolio.

---

##  Day 1

###  Goals Completed
- [x] Installed Python 3.13.7 and set up virtual environment
- [x] Set up VSCode + pip
- [x] Created GitHub repo + .gitignore
 
### 📝 DSA Problems Solved

1. **Two Sum (#1, Easy)**  
   - Approach: Use hash map to store seen numbers; check for complement  
   - Time Complexity: O(n), Space Complexity: O(n)  
   - Code: `/DSA/Day1/two_sum.py`

 2. **Contains duplicate elements(#217,Easy)**
      - Apprroach:
      1. convert the given  list into set
      2. compare the length of set and length of list
      3. if length of set  less than the length of list
      4. then it contains the duplicate else it does not contain duplicates
    - Time Complexity: O(N),Space Complexity: O(N)
 3. **Median of a array(greeks for greeks)**
    
    -Apprroach
    1. If the list length is odd, the median is the middle element.
    2. If the list length is even, the median is the average of the two middle elements.
    3. Time Complexity: O(n log n) ,space complexity: O(n)
    4.  asked in Accolite, Amazon, Samsung , FactSet
  ##  Day 2
1. **Second largest element (greeks for greeks)**
    -Apprroach
    1.  The goal is to find the second biggest number in a list of numbers.
    2. First, we look for the biggest number.
    3. Then, we look again for the biggest number that’s not the first one.
    4. If we don’t find a second biggest (like if all numbers are the same), we return -1.
    5. Time complexity is O(n) and space complexity is O(1)
    6. asked in SAP LabsRockstand


###  Python / Tools Learned
- Python 3.13.7 installed  
- Virtual environment setup (`venv`)  
- VSCode configuration  
- `requirements.txt` creation

###  Notes / Reflection
- Key learning: GitHub workflow, structuring repo, Python environment setup  
- Struggled with: None
- Next steps: Continue DSA problems, explore more Python concepts, start mini-projects
