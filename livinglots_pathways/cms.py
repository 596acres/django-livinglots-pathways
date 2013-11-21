from feincms.content.application import models as app_models
from feincms.module.mixins import ContentModelMixin


class PathwayFeinCMSMixin(ContentModelMixin):

    @app_models.permalink
    def get_absolute_url(self):
        return ('pathway_detail', 'pathways.urls', (), {
            'slug': self.slug,
        })
