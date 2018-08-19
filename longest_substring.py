"""
Problem : Given a string, find the length of the longest substring without repeating characters.


Example 1:
    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", which the length is 3.

Example 2:
    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
                 Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def __init__(self):
        """ user-defined input string """
        self.input = None
        self.unique_substrings = []
        self.non_rep_substring = ''

    def get_input_string(self):
        return self.input

    def find_non_repeating_substrings(self):
        """
        self.input is validated
        :return: None if self.input is None or ""
                1 if self.input is of length 1
                'continue' otherwise
        """
        temp_substring = ""

        if self.input is None or self.input is "":
            print('Blank input')
            return None
        elif len(self.input) == 1:
            return 1
        else:
            temp_substring = self.input[0]
        print('--------------------------------------\n')

        # We have already stored the 1st char in temp_substring
        #   So, start from 2nd to len(self.input)
        for i in range(1, len(self.input)):
            print('\t temp_substring : ', temp_substring)
            print('\t --- self.input[i] : ', self.input[i])
            # if self.input[i] != self.input[i-1]:
            #     temp_substring += self.input[i]
            if self.input[i] not in temp_substring:
                temp_substring += self.input[i]
            else:
                # self.unique_substrings.append(temp_substring)
                # # print('\t self.unique_substrings : ', self.unique_substrings)
                # temp_substring = ""
                # temp_substring += self.input[i]
                print('--------------------------------------\n')
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        print('\t temp_substring : ', temp_substring)
        self.non_rep_substring = temp_substring
        if temp_substring not in self.unique_substrings:
            self.unique_substrings.append(temp_substring)
        print('self.unique_substrings : ', self.unique_substrings)
        return temp_substring

    def lengthOfLongestSubstring(self, input_string):
        """
        :type input_string: string (user input)
        :rtype: int (length of the longest substring without repeating characters)
        """
        self.input = input_string
        print('User input : ', self.input)
        validate_n_create_unique_substrings = self.find_non_repeating_substrings()
        if validate_n_create_unique_substrings is None:
            return 0
        elif validate_n_create_unique_substrings == 1:
            return 1
        print('validate_n_create_unique_substrings : ', validate_n_create_unique_substrings)
        print('self.unique_substrings : ', self.unique_substrings)
        temp_longest_substring = None
        max_length = 0
        for substring in self.unique_substrings:
            # print('processing : ', substring)
            if len(substring) > max_length:
                max_length = len(substring)
                temp_longest_substring = substring

        # print('--------------------------------------\n')
        # print('temp_longest_substring : ', temp_longest_substring)
        # print(' max_length : ', max_length)
        return max_length


# input = 'abcabcbb'
# exp_out = 3
# input = 'bbbbb'
# exp_out = 1
input = 'pwwkew'
exp_out = 3
# input = ""
# exp_out = 0
# input = None
# exp_out = 0
# input = " "
# exp_out = 1
# input = "a"
# exp_out = 1
# input = "au"
# exp_out = 2
# input = "aubcxyz"
# exp_out = 7
# input = "aab"
# exp_out = 2
# input = "dvdf"
# exp_out = 3
ans = Solution()
curr_out = ans.lengthOfLongestSubstring(input)
print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
print('your output : ', curr_out)
if curr_out != exp_out:
    print('expected output : ', exp_out)
    print('ERRRRRRRROOR')
