pool = int(input())
pipe_one_debit = int(input())
pipe_two_debit = int(input())
worker = float(input())

pipe_one = pipe_one_debit * worker
pipe_two = pipe_two_debit * worker
pipes_combined = pipe_one + pipe_two

pipe_one_contribution = (pipe_one / pipes_combined) * 100
pipe_two_contribution = (pipe_two / pipes_combined) * 100

pool_filled = (pipes_combined / pool) * 100

if pool >= pipes_combined:
    print("The pool is " + f'{pool_filled:.2f}' + "% full. Pipe 1: " + f'{pipe_one_contribution:.2f}' + "%. Pipe 2: " + f'{pipe_two_contribution:.2f}' + "%.")
else:
    print("For " + f'{worker:.2f}' + " hours the pool overflows with " + f'{pipes_combined-pool:.2f}' + " liters.")