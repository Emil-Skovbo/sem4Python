import selenium_gutenberg
res = selenium_gutenberg.get_info('sherlock holmes conan')
res

print(
'There were {} Hartmanns on the first page'.format(len(res)))

selenium_gutenberg.save_to_file(''.join(res))