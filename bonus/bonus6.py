contents = ['Go chicago cubs', 
            'The Chicago Cubs will win the world series this year. Mark my words for it.', 
            'Cody Bellinger, Mark Busch, and Dansby Swanson will carry the Cubs to a World Series championship']

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for content, filename in zip(contents, filenames):
    file = open(f'../files/{filename}', 'w')
    file.write(content)

