### Fig 1. Class Diagram
![eb93fdb26af78f33ab469af9e1106111](https://user-images.githubusercontent.com/45643520/141032334-4351df26-c733-4c5a-9cba-ea9e78722919.png)

The cat class will have attributes like name, sex, alteration status, picture, etc., as well as get methods for the attributes. The colony class will have some kind of identification number, street name, number of volunteers at that location, and shelter box count, as well as get methods for the attributes. The above class diagram highlights the relationship between cat and colony. For each colony, there can be one or more cats. Each colony can have one or more cats, however, each cat can only belong to one colony. Additionally, there are the volunteer and director classes. The director class will have a name and rescue contacts, with get methods. The volunteer class will have name, colony assignments, and supply status, as well as get methods.

### Fig 2. Sequence Diagram #1: Submitting Volunteer Form
![sequence diagram one](https://github.com/CIS3296SoftwareDesignF21/prj-04-templecats/blob/valKeo-week3md/sq1.png)

The above sequence diagram demonstrates the communication between user and website application when a volunteer form is submitted. The user first navigates to the volunteer or form tab on frontend, which then communicates the form submission to the backend, which will then write the form information to the database. The backend will return a notification that the write was completed to the frontend, which will then give the user a confirmation message that form submission was successful.

### Fig 3. Sequence Diagram #2: Donation
![sequence diagram two](https://github.com/CIS3296SoftwareDesignF21/prj-04-templecats/blob/valKeo-week3md/sq2.png)

The above sequence diagram demonstrates the communication between user and website application when a user wants to donate supplies. The user will first click on the donation tab on the temple cats website. There, they will find the Amazon Wishlist link, that when clicked, will redirect the user to Amazon to complete the donation purchase.
