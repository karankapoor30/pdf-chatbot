css = """
<style>
.bot-message {
    background-color: #f1f1f1;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
    color: black;
}
.user-message {
    background-color: #007bff;
    color: white;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
    text-align: right;
}
</style>
"""

bot_template = """
<div class="bot-message">
    {{MSG}}
</div>
"""

user_template = """
<div class="user-message">
    {{MSG}}
</div>
"""
