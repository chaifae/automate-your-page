# These functions will take the notes I've written and format them
# with some HTML structure. I'll still have to do some minor other
# formatting, but the bulk of the work is done automatically.

# Here are my notes that will be used to generate the HTML:
# Notes are shortened for brevity
my_notes = [ ['Basics of Web and HTML', 'The World Wide Web is a collection of documents'],
             ['Creating s Structured Document with HTML', 'HTML is the structure of a webpage.'],
             ['Adding CSS Style to HTML Structure', 'CSS creates the style of a webpage.'],
			 ['Telling Computers What to Do', 'A computer is a universal machine, that means it can be programmed to do anything we want it to do.'],
			 ['Variables and Strings', 'A variable is a way to give a name to a value so you can easily reference and use that value later.'],
			 ['Functions', 'Functions take input, do something with the input, and then produce output.'],
			 ['Repetition, Loops, and Structured Data', 'if, while, lists, and for loops'],
			 ['How to Solve Problems', 'The first step to solving any problem is to understand the inputs and outputs.'] ]



def generate_concept_HTML(concept_title, concept_notes):
	# this will generate the HTML for a single concept, using the
	# title and notes passed into the function
    html1 = '''
<div class="lesson">
    <h2>
        ''' + concept_title
    html2 = '''
    </h2>
    <div class="notes">
	''' + concept_notes
    html3 = '''
    </div>
</div>'''
    
    full_html = html1 + html2 + html3
    return full_html


def make_HTML(concept):
	# this function takes a concept passed into it and extracts the 
	# title and notes to input them into generate_concept_HTML
    title = concept[0]
    notes = concept[1]
    return generate_concept_HTML(title, notes)


def make_HTML_all_concepts(list_of_concepts):
	# this function will loop over the concepts in the list, plug
	# the concepts into the make_HTML function, and then combine all
	# the output into all_html, which it returns
    all_html = ''
    for concept in list_of_concepts:
        concept_html = make_HTML(concept)
        all_html += concept_html
    return all_html

	
# printing the outputs of this function will generate all the HTML
# I need for my notes
print make_HTML_all_concepts(my_notes)