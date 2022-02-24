import os

os.chdir('O:\Plant\Engineering\EMA Work Instructions\Work Instruction - Final Complete Modifiable')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)

    if file_name.count('-') == 4:
        f_map, f_dep, f_ref, f_part, f_num = file_name.split('-')
        new_name = '{}-{}-{}-{}-{}{}'.format(f_part, f_num, f_map, f_dep, f_ref, file_ext)

        os.rename(f, new_name)

    if file_name.count('-') == 5:
        f_map, f_dep, f_ref, f_part, f_part2, f_num = file_name.split('-')
        new_name = '{}-{}-{}-{}-{}-{}{}'.format(f_part, f_part2, f_num, f_map, f_dep, f_ref, file_ext)

        os.rename(f, new_name)

    if file_name.count('-') == 6:
        f_map, f_dep, f_ref, f_part, f_part2, f_part3, f_num = file_name.split('-')
        new_name = '{}-{}-{}-{}-{}-{}-{}{}'.format(f_part, f_part2, f_part3, f_num, f_map, f_dep, f_ref, file_ext)

        os.rename(f, new_name)