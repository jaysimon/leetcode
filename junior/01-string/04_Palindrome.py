def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    cap = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new_char = []
    for char in s:
        if char in cap:
            new_char.append(cap.index(char))
        if char in low:
            new_char.append(low.index(char))
    flag = True
    print(new_char)
    for i in range(len(new_char)/2):
		if(new_char[i] != new_char[len(new_char)-i-1]):
			flag = False
    return flag


def main():
    sInput1 = "A man, a plan, a canal: Panama"
    sInput2 = "race a car"
    print(isPalindrome(sInput1))

if __name__ == "__main__":
	main()
