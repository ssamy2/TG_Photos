import json

def verify_gift_ids():
    ss_path = r"C:\Users\Sami\Desktop\TG_Photos\ss.json"
    gifts_details_path = r"C:\Users\Sami\Desktop\TG_Photos\Gifts_Details.json"
    
    with open(ss_path, 'r', encoding='utf-8') as f:
        ss_data = json.load(f)
    
    with open(gifts_details_path, 'r', encoding='utf-8') as f:
        gifts_details = json.load(f)
    
    ss_ids = {gift['id'] for gift in ss_data if gift.get('type') == 'REGULAR'}
    
    upgraded_ids = {gift['regular_id'] for gift in gifts_details['upgraded']}
    unupgraded_ids = {gift['id'] for gift in gifts_details['unupgraded']}
    
    all_gifts_details_ids = upgraded_ids | unupgraded_ids
    
    missing_in_gifts_details = ss_ids - all_gifts_details_ids
    extra_in_gifts_details = all_gifts_details_ids - ss_ids
    
    print("=" * 60)
    print("تقرير التحقق من IDs الهدايا")
    print("=" * 60)
    print(f"\nعدد الهدايا في ss.json: {len(ss_ids)}")
    print(f"عدد الهدايا في Gifts_Details.json (upgraded): {len(upgraded_ids)}")
    print(f"عدد الهدايا في Gifts_Details.json (unupgraded): {len(unupgraded_ids)}")
    print(f"المجموع الكلي في Gifts_Details.json: {len(all_gifts_details_ids)}")
    
    if missing_in_gifts_details:
        print(f"\n❌ هدايا موجودة في ss.json لكن مفقودة من Gifts_Details.json ({len(missing_in_gifts_details)}):")
        for gift_id in sorted(missing_in_gifts_details):
            gift_info = next((g for g in ss_data if g['id'] == gift_id), None)
            if gift_info:
                print(f"  - ID: {gift_id}, Name: {gift_info.get('full_name', 'N/A')}")
    else:
        print("\n✅ جميع الهدايا من ss.json موجودة في Gifts_Details.json")
    
    if extra_in_gifts_details:
        print(f"\n⚠️ هدايا موجودة في Gifts_Details.json لكن مفقودة من ss.json ({len(extra_in_gifts_details)}):")
        for gift_id in sorted(extra_in_gifts_details):
            if gift_id in upgraded_ids:
                gift_info = next((g for g in gifts_details['upgraded'] if g['regular_id'] == gift_id), None)
                section = "upgraded"
            else:
                gift_info = next((g for g in gifts_details['unupgraded'] if g['id'] == gift_id), None)
                section = "unupgraded"
            if gift_info:
                print(f"  - ID: {gift_id}, Name: {gift_info.get('full_name', 'N/A')} ({section})")
    else:
        print("\n✅ لا توجد هدايا إضافية في Gifts_Details.json")
    
    print("\n" + "=" * 60)
    
    if not missing_in_gifts_details and not extra_in_gifts_details:
        print("✅ التحقق ناجح: جميع IDs متطابقة تماماً!")
        return True
    else:
        print("❌ يوجد اختلافات بين الملفين")
        return False

if __name__ == "__main__":
    verify_gift_ids()
