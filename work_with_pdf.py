with open('Smyk-tyndyk.pdf', mode='br') as my_file, open('new_git.pdf', mode='bw') as new_git_file:
    content = my_file.read()
    new_git_file.write(content)
