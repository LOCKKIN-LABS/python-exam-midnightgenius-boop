def main():
  
    user_input = int(input()) 
    n=int(user_input)
    
    # --- DO NOT TOUCH THIS LINE ---
    # TODO: Implement core logic here
    # --- DO NOT TOUCH THIS LINE ---
    pass
if n % 3 == 0:
    output = "Alpha"
elif n % 5 == 0:
    output = "Beta"
if output == "":
    output = str(n)  
print(output)
if __name__ == "__main__":
    main()
