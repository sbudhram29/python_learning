from collections import Counter

def min_window(s, t):
	if not t or not s:
		return ""

	chars_dict = Counter(t)
	required = len(chars_dict)

	left, right = 0, 0

	current_valid = 0

	current_chars = {}

	result = float('inf'), None, None

	while right < len(s):
		c = s[right]
		current_chars[c] = current_chars.get(c, 0) + 1

		if c in chars_dict and current_chars[c] == chars_dict[c]:
			current_valid += 1

		while left <= right and current_valid == required:
			c = s[left]

			if right - left + 1 < result[0]:
				result = right-left +1, left, right

			current_chars[c] -= 1

			if c in chars_dict and current_chars[c] < chars_dict[c]:
				current_valid -= 1

			left += 1
		right += 1

	if result[0] == float('inf'):
		return ""

	return s[result[1]: result[2] + 1]



S = "xyyzyzyx"
T = "xyz"

print(min_window(S, T))