from mylibrary import file_movement as fm

for files in fm.search_files('/Users/sanjaybiswas/Downloads', 'csv'):
    print(f" ---{files}")

#fm.delete_files(fm.search_files('/Users/sanjaybiswas/Downloads', 'chartink_AllInOne'))