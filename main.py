# LIMITATION: BERT is limited to 512 tokens: https://github.com/huggingface/transformers/issues/1791

import pandas as pd
import numpy as np
import torch
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer

model = BertForQuestionAnswering.from_pretrained(
    "bert-large-uncased-whole-word-masking-finetuned-squad"
)
tokenizer = BertTokenizer.from_pretrained(
    "bert-large-uncased-whole-word-masking-finetuned-squad"
)


def question_answer(question, text):

    # tokenize question and text as a pair
    input_ids = tokenizer.encode(question, text)

    # string version of tokenized ids
    tokens = tokenizer.convert_ids_to_tokens(input_ids)

    # segment IDs
    # first occurence of [SEP] token
    sep_idx = input_ids.index(tokenizer.sep_token_id)
    # number of tokens in segment A (question)
    num_seg_a = sep_idx + 1
    # number of tokens in segment B (text)
    num_seg_b = len(input_ids) - num_seg_a

    # list of 0s and 1s for segment embeddings
    segment_ids = [0] * num_seg_a + [1] * num_seg_b
    assert len(segment_ids) == len(input_ids)

    # model output using input_ids and segment_ids ==> Max 512 tokens
    output = model(
        torch.tensor([input_ids]), token_type_ids=torch.tensor([segment_ids])
    )

    # reconstructing the answer
    answer_start = torch.argmax(output.start_logits)
    answer_end = torch.argmax(output.end_logits)
    if answer_end >= answer_start:
        answer = tokens[answer_start]
        for i in range(answer_start + 1, answer_end + 1):
            if tokens[i][0:2] == "##":
                answer += tokens[i][2:]
            else:
                answer += " " + tokens[i]

        if answer.startswith("[CLS]"):
            answer = "Unable to find the answer to your question."

        print("\nPredicted answer:\n{}".format(answer.capitalize()))


# Limited to 512 tokens
text = """
This Privacy Policy outlines our practices for collecting, using, maintaining, protecting and disclosing
Customer Data, including Personal Data, through Genesys Cloud, and what we do with that
information. Additionally this Privacy Policy describes the privacy principles followed by Genesys
Telecommunications Laboratories, Inc. (“Genesys”) with respect to international transfers of Personal
Data (defined below). If you have questions about this Privacy Policy, or how we respect your
information, contact us at DataPrivacy@genesys.com. For the purposes of this Privacy Policy,
“Customer Data” means the Genesys customer’s proprietary information and information about its
customers (including Personal Data) submitted through Genesys Cloud by the customer and its
agents. Customer Data does not include aggregate data and information related to the performance,
operation and use of the Cloud Services. “Personal Data” means any information relating to
individuals that is protected by applicable privacy law.
What Customer Data does Genesys collect through the Genesys Cloud services?
In general, Genesys Cloud manages consumer engagements via various media channels. Genesys
Cloud processes information related to the consumer engagements (audio call recordings, call metadata, chat messages, etc.). Genesys Cloud also collects information that a customer organization
already stores by connecting with services such as Active Directory and Customer Relationship
Management (CRM) software. Additionally, a customer may choose to provide information to Genesys
Cloud, such as through importing information from third party websites, uploading files, screensharing,
video or audio calls, or chat messages.
Genesys will only collect Customer Data when it is voluntarily made available to us by a customer.
How may Genesys use Personal Data collected through the Genesys Cloud services?
Genesys will use this information to provide Genesys Cloud services. If recording is enabled, Genesys
will collect and store interaction recordings. Genesys also uses some Personal Data to route calls or
webchats and maintain records of these interactions. There are additional functions that Genesys
Cloud can provide. For example, Genesys Cloud can facilitate a customer agent to share files with
other members of their organization. As another example, a customer agent may share their screen
with other members of the organization.
"""

question = input("\nPlease enter your question: \n")
while True:
    question_answer(question, text)

    flag = True
    flag_N = False

    while flag:
        response = input(
            "\nDo you want to ask another question based on this text (Y/N)? "
        )
        if response[0] == "Y":
            question = input("\nPlease enter your question: \n")
            flag = False
        elif response[0] == "N":
            print("\nBye!")
            flag = False
            flag_N = True

    if flag_N == True:
        break
