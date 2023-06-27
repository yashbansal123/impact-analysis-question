def findProbability(number):
        days = 4
        memo = {}
        def  dfs(n, d):
            key = "{n}:{d}".format(n=n,d=d)
            if key in memo:
                return memo[key]
            # print("F", n, d)
            if d == 0:
                return 0
            elif n == 0:
                return 1
                
            result =  dfs(n - 1, days) + dfs(n - 1, d-1)
            memo[key] = result
            return result
        return "{B}/{A}".format(B= dfs(number-1, days-1), A= dfs(number, days))
    


print(findProbability(5))

print(findProbability(10))





"""
This is an explaination for the answer.

Here number represents the number of days and 'days' represent currently allowed days in a row to be absent.

If we start from end of the days, i.e., from the day of graduation, for solving part A:
Number of days allowed  = 'number'
number of leaves allowed in a row = 'days'

At each day, we have a choice, either we take a leave or we attend the class,
    case 1 : if we take a leave, we have 'days - 1' leaves left to be taken in a row while number of days become 'number - 1'
    case 2 : if we attend class, we now have total 'days' leaves left since it resets for each attendance, and number of days become 'number-1'

by iterating from last day to first using recurrsion, we can calculate this probability.

For Part B:
We just need to assume that person is absent on graduation day, i.e., at the very last day and calculate the solution from that assumption,
this makes the following changes:
    change 1 : the number of days reduce by 1 as last day is already taken care of.
    change 2 : the number of allowed leaves also reduce by 1 since on last day, person is already absent.


"""