def total_salary(path: str) -> tuple:

    # Initialize starting values for salary_total and salary_average
    salary_total = 0
    salary_average = 0
    # Initialize counter to calculate salary_average     
    cnt = 0
    try:
        # Open file in read mode
        with open(path, 'r') as f:
            # Read all lines in array
            lines = f.readlines()

            # Walk through all lines in a loop
            for line in lines:
                try:
                    # Increase counter by 1 by default for every line
                    cnt += 1

                    # Calculate salary_total
                    salary_total += float(line.split(',')[-1])
                except ValueError:
                    # In case ValueError counter needs to be decreased by 1 
                    cnt -= 1
        # Recalculate salary_average
        try:
            salary_average = salary_total / cnt 
        except ZeroDivisionError:
            print(f'Please check for denominator value. It should not be equal to zero!')
    except FileNotFoundError:
        print(f'There is no such file as {path}')

    except UnicodeDecodeError:
        print(f"Cannot read {path} due to encoding issue")
        return None

    except OSError as e:
        print(f"There has been another issue {e} while working with {path}")
    return salary_total, salary_average

total, average = total_salary('text_1.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
total, average = total_salary('text1.txt')