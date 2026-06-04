def build_email_template(items):

    header = """
    <div style="font-family:Arial; font-size:14px; color:#333; line-height:1.5">
        <h3>📌 Νέες Ανακοινώσεις EOPPEP</h3>
    """

    body = ""

    for item in items:
        body += f"""
        <div style="margin-bottom:12px;">
            <b>{item['title']}</b><br>
            <a href="{item['url']}">{item['url']}</a>
        </div>
        """

    footer = """
    </div>
    """
    
    return header + body + footer