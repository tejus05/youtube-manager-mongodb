from pymongo import MongoClient
from bson import ObjectId

url = "mongodb+srv://tejus05:tejus05@freetier.t3xa6nw.mongodb.net/?retryWrites=true&w=majority&appName=FreeTier"

client = MongoClient(url, tlsAllowInvalidCertificates=True)

db = client["ytmanager"]

video_collection = db["videos"]

def list_all_videos():
  for video in video_collection.find():
    print(f"ID: {video['_id']}, Name: {video["name"]}, Time: {video["time"]}")

def add_video():
  name = input("Enter video name: ")
  time = input("Enter video time: ")
  video_collection.insert_one({"name":name,"time":time})
  

def update_video():
  name = input("Enter video name: ")
  time = input("Enter video time: ")
  id = ObjectId(input("Enter video id to be updated: "))
  video_collection.update_one(
    {
      '_id':id
    },
    {
      "$set": {
        "name": name,
        "time": time,
      }
    }
  )

def delete_video():
  id = ObjectId(int(input("Enter the video to be deleted: ")))
  video_collection.delete_one({
    "_id": id
  })

def main():
  
  while True:
    print("Youtube Manager")
    print("1. List all youtube videos")
    print("2. Add a youtube video")
    print("3. Update a youtube video detail")
    print("4.Delete a youtube video")
    print("5. Exit")
    choice = input("Enter your choice: ")
    
    match choice:
      case '1':
        list_all_videos()
      case '2':
        add_video()
      case '3':
        update_video()
      case '4':
        delete_video()
      case '5':
        break
      case _:
        print("Invalid Choice")

if __name__ == "__main__":
  main()