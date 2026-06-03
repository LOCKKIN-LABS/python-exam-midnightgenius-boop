def main():
  
    user_input = int(input()) 
    
    # --- DO NOT TOUCH THIS LINE ---
    # TODO: Implement core logic here
    # --- DO NOT TOUCH THIS LINE ---
    pass
if user_input % 3==0 and user_input % 5==0:
    print("AlphaBeta")
elif user_input % 3==0:
    print("Alpha")
elif user_input % 5==0:
    print("Beta")
else:
    print(user_input)
if __name__ == "__main__":
    main()
