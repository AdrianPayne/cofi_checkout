import setuptools

setuptools.setup(
    name="cofi_checkout",
    version="0.1.0",
    url="https://github.com/adrianpayne/cofi_checkout",
    author="Adrian Sacristan",
    author_email="adriansacristan1993@gmail.com",
    description="Checkout class to allow scanning of products and applying of discounts",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    include_package_data=True,
    package_data={'': ['data/products_and_discounts.json']},
)