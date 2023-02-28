from pathlib import Path
from flask import Flask, render_template, request
from utils.utils import title_match, load_wapo

app = Flask(__name__)

DATA_DIR = Path(__file__).parent.joinpath("pa2_data")
wapo_path = DATA_DIR.joinpath("wapo_pa2.jl")
wapo_docs = load_wapo(wapo_path)  # load and process WAPO documents
global_matched=[] #stores the remaining documents as user gets to the next page

@app.route("/")
def home():
    """
    home page
    :return:
    """
    return render_template("home.html")


@app.route("/results", methods=["POST"])
def results():
    """
    result page
    :return:
    """
    global global_matched
    query_text = request.form["query"]  # Get the raw user query from home page
    
    # compare query_text with every document title using utils.title_match()
    # matched_id_list stores all documents with the corresponding titles 
    matched_id_list = []
    for key, value in wapo_docs.items():
        if title_match(query_text, value['title']): # look at the title
            matched_id_list.append(value) 
    match_num = len(matched_id_list)

    # prepare first 8 documents for display
    page_count = 0
    first_matches = matched_id_list[page_count: page_count+8]

    # remove first 8 documents from global_matched
    global_matched = matched_id_list[8:]

    # only set page_flag to True if there are more than 8 matched documents
    page_flag = False
    if match_num-8 > 1:
        page_flag = True
    
    # pass arguments to render_template()
    return render_template("results.html", matched_list=first_matches, match=match_num, query=query_text, page_count=page_count, page_flag=page_flag)  # add variables as you wish


@app.route("/results/<int:page_id>", methods=["POST"])
def next_page(page_id):
    """
    "next page" to show more results
    :param page_id:
    :return:
    """
    global global_matched

    # increment page_id to display in route /results/<int:page_id>
    page_id += 1 

    # prepare first 8 entries of the remaining documents for rendering
    first_matches = global_matched[:8]

    # only set page_flag to True if more than 8 matched documents are left
    page_flag = False 
    if len(global_matched)>8:
        page_flag = True

    # remove first 8 documents from global_matched
    global_matched = global_matched[8:]

    # pass arguments to render_template()
    return render_template("results.html", matched_list=first_matches, page_count=page_id, page_flag=page_flag)  # add variables as you wish


@app.route("/doc_data/<doc_id>")
def doc_data(doc_id):
    """
    document page
    :param doc_id:
    :return:
    """

    # use doc_id key to get document value from wapo_docs
    item = wapo_docs[doc_id]

    return render_template("doc.html", item=item)  # add variables as you wish


if __name__ == "__main__":
    app.run(debug=True, port=5000)