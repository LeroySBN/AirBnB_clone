# The AirBnB clone project (ongoing)

**Tech Stack: Python, HTML5, CSS3**

![airbnb](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/d2d06462824fab5846f3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230219%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230219T095410Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=93a2bd00a5513c46c54dd5ca7f7b1e0f73a350354241427246af82115c41d2c7)

***

**Data diagram**

![airbnb-dd](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/99e1a8f2be8c09d5ce5ac321e8cf39f0917f8db5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230219%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230219T095410Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c17cf0359b7db963b44fc9d73d232b736fe3c8d76940ee1adc617f4ec0364e97)

***

**Files and Directories**

* `models` directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
* `tests` directory will contain all unit tests.
* `console.py` file is the entry point of our command interpreter.
* `models/base_model.py` file is the base class of all our models. It contains common elements:

++ attributes: `id, created_at and updated_at`
++ methods: `save()` and `to_json()`

* `models/engine` directory will contain all storage classes (using the same prototype).
