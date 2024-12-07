from pathlib import Path

current_directory = Path(__file__).parent # Get the directory of the running python script
page_pairs_path = current_directory / 'pagepairs.txt' # Join the directory with the file name
updates_path = current_directory / 'updates.txt' # Join the directory with the file name
page_pairs_str = page_pairs_path.read_text()
updates_str = updates_path.read_text()

page_pairs = {tuple(pair.split("|")) for pair in page_pairs_str.split("\n")}
updates = [tuple(update_chain.split(",")) for update_chain in updates_str.split("\n")]

"""Iterates through the chain of pages to be updated, seeing if any pair violations occur
   Returns the middle page if the chain is valid, 0 otherwise"""

def update_is_valid(page_pairs, update_chain): #Make this return a boolean
    prev_pages = set() # Tracks what pages have been printed before in this chain

    # Checks whether the pages that shouldn't have come prior, have come prior
    for printed_page in update_chain:
        # Set of pages that shouldn't have come prior
        mini_set = {pair[1] for pair in page_pairs if pair[0] == printed_page}

        if prev_pages & mini_set: # Checks for overlap between the two sets
            return False # Reject update chain
        
        prev_pages.add(printed_page) # Add the printed page to the set of previous pages

    return True # Accept update chain if there are no conflicts


"""Iterates through the update chains, summing the middle pages of the update sequences"""

def sum_and_reject(page_pairs, updates):
    page_sum = 0
    rejected_chains = [] # List of rejected update chains for part 2

    for update_chain in updates:
        if update_is_valid(page_pairs, update_chain):
            page_sum += int(update_chain[len(update_chain)//2]) # Add the middle page to the sum

        else:
            rejected_chains.append(update_chain) # Add the rejected chain to the list for part 2
        
    return page_sum, rejected_chains

"""Uses a merge sort to reorder the page numbers so that they are in the correct order
   Caveat: Ignores multiple valid chains and only returns the first valid chain"""

def merge_sort(page_pairs, chain):
    # print(chain)

    if update_is_valid(page_pairs, chain): # Skip sorting if the chain is already valid
        return chain

    def merge_with_check(page_pairs, left, right): # Bounce between left and right lists to add valid pages 
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            # # As it passes through both candidates at the same time, it checks for the pair in both directions
            if update_is_valid(page_pairs, merged + [left[i]] + [right[j]]):
                merged.append(left[i])
                i += 1
            elif update_is_valid(page_pairs, merged + [right[j]]):
                merged.append(right[j])
                j += 1
            else: 
                raise ValueError("Contradicting rule or cyclical dependency detected.")
            
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
            
    if len(chain) <= 1: # Simplest case of a chain of length 1 is already sorted
            return chain
        
    mid = len(chain) // 2
    left = merge_sort(page_pairs, chain[:mid]) # Feed each mini chain back into the merge sort to break it down further
    right = merge_sort(page_pairs, chain[mid:]) # The breakdowns keep occuring until the mini chains are of length 1 before merging

    return merge_with_check(page_pairs, left, right) # Merge the mini chains back together

def fix_rejected_updates(page_pairs, broken_chains):

    fixed_chains = []
    for chain in broken_chains:
        fixed_chain = merge_sort(page_pairs, chain)
        fixed_chains.append(fixed_chain)
    return fixed_chains

def spit_sums(page_pairs, updates):
    sum_and_rejected = sum_and_reject(page_pairs, updates) # Part 1
    fixed = fix_rejected_updates(page_pairs, sum_and_rejected[1]) # Part 2
    fixed_sum = sum_and_reject(page_pairs, fixed)

    # print(fixed_sum[1]) # Debug: List should be empty if all chains are fixed

    return sum_and_rejected[0], fixed_sum[0]

print(spit_sums(page_pairs, updates))

# test_page_pairs_str = """47|53 # Test case
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13"""

# test_updates_str = """75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""

# test_page_pairs = {tuple(pair.split("|")) for pair in test_page_pairs_str.split("\n")}
# test_updates = [tuple(update_chain.split(",")) for update_chain in test_updates_str.split("\n")]

# print(spit_sums(test_page_pairs, test_updates)) 



