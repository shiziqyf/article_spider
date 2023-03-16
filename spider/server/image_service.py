from dao.imageDAO import ImageDAO
from dao.model.image_resource import ImageResource


def save_image(image: ImageResource):
    old_image = ImageDAO.queryOneByUrl(image.url)
    if old_image is None:
        ImageDAO.insert(image)
    else:
        ImageDAO.updatedById(old_image.id, image)
