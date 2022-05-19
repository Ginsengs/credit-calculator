import argparse
import sys
import math


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str)
    parser.add_argument("--principal", type=float)
    parser.add_argument("--periods", type=float)
    parser.add_argument("--interest", type=float)
    parser.add_argument("--payment", type=float)
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))


def calc(args):
    if args.interest is None:
        return "Incorrect parameters."
    elif args.interest is not None:
        if args.type == 'diff':
            diff_list = []
            args.interest = args.interest / 100
            i = args.interest / 12 * (100 / 100)
            for num in range(int(args.periods)):
                months = num + 1
                diff = math.ceil(args.principal / args.periods + i * (
                        args.principal - (args.principal * (months - 1) / args.periods)))
                diff_list.append(diff)
                print(f"Month {num + 1}: payment is {diff_list[num]}")
            print('\n')
            overpayment = round(sum(diff_list) - args.principal)
            return f"Overpayment = {overpayment}"
        elif args.type == 'annuity':
            if args.principal is None:
                i = args.interest / 12 / 100
                principal = math.floor(
                    args.payment / ((i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1)))
                print(f"Your loan principal = {principal}!")
                overpayment = math.floor((args.payment * args.periods) - principal)
                return f"Overpayment = {overpayment}"

            elif args.periods is None:
                args.interest = args.interest / 100
                i = args.interest / 12 * 1
                n = math.ceil(math.log(float(args.payment) / (float(args.payment) - i * float(args.principal)), i + 1))
                years, months = (n // 12, n % 12)
                if years == 0:
                    if months == 1:
                        print(f'It will take {months} month')
                    else:
                        print(f'It will take {months} months to repay this loan!')

                elif months == 0:
                    if years == 1:
                        print(f'It will take {years} year to repay this loan!')
                    else:
                        print(f'It will take {years} years to repay this loan!')
                else:
                    print(f'It will take {years} years and {months} months to repay this loan!')
                overpayment = math.ceil(args.payment * (years * 12) - args.principal)
                return f"Overpayment = {overpayment}"

            elif args.payment is None:
                args.interest = args.interest / 100
                i = args.interest / 12 * 1
                args.payment = math.ceil(
                    args.principal * ((i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1)))
                print(f'Your annuity payment = {args.payment}!')
                overpayment = math.ceil((args.payment * args.periods) - args.principal)
                return f"Overpayment = {overpayment}"


if __name__ == '__main__':
    main()
