# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app
from services.publications import create_publication,update_publication,delete_publication,get_all_publications,get_publication_by_id
from services.blog import create_blog,update_blog,delete_blog,get_all_blogs,get_blog_by_id
from services.club_talk import create_card,update_card,delete_card,get_all_cards,get_card_by_id
from services.about_us import create_member,update_member,delete_member,get_all_members,get_member_by_id
from services.gallery import create_memory,delete_memory
from services.banner import upload_banner
from services.home import create_block,update_block,delete_block,get_all_blocks,get_block_by_id
from services.contributions import create_contribution,update_contribution,delete_contribution,get_all_contributions,get_contribution_by_id
from services.feedback import create_feedback,update_feedback,delete_feedback,get_all_feedbacks,get_feedback_by_id

initialize_app()

@https_fn.on_request()
def on_request_example(req: https_fn.Request) -> https_fn.Response:
    return https_fn.Response("Hello world!")

