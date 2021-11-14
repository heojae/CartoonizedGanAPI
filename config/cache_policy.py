def apply_cache_policy(app):
    @app.after_request
    def add_nocache_header(response):
        """
        cache가 생성이 되어, 이미지의 이름을 browser에 기록이 되어,
        수정한 정보가 업로드 되지 않는 경우가 있어, 그것을 대비하여 작성을 해두었습니다.
        특히, swagger(API_document.ymal)를 수정을 할때 위 현상이 생기므로 작성을 해두었습니다
        """
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        response.headers["Expires"] = '0'
        response.headers["Pragma"] = "no-cache"
        return response
