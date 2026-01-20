def analyze_answers(answers):
    scores = {
        'Software Developer': 0,
        'Data Analyst': 0,
        'UI/UX Designer': 0,
        'Cybersecurity Expert': 0,
        'Digital Marketer': 0,
        'Cloud Engineer': 0
    }

    for ans in answers:
        if not ans:
            continue
        ans = ans.lower()
        if any(k in ans for k in ['coding', 'programming', 'software']):
            scores['Software Developer'] += 2
            scores['Cloud Engineer'] += 1
        if any(k in ans for k in ['data', 'analysis', 'excel']):
            scores['Data Analyst'] += 2
        if any(k in ans for k in ['design', 'creativity', 'ui', 'ux']):
            scores['UI/UX Designer'] += 2
        if any(k in ans for k in ['security', 'network', 'cybersecurity']):
            scores['Cybersecurity Expert'] += 2
        if any(k in ans for k in ['marketing', 'social media', 'advertising']):
            scores['Digital Marketer'] += 2

    best_role = max(scores, key=scores.get)

    descriptions = {
        'Software Developer': 'Develop and maintain software applications.',
        'Data Analyst': 'Analyze data to derive actionable insights.',
        'UI/UX Designer': 'Design user interfaces and experiences.',
        'Cybersecurity Expert': 'Protect systems from cyber threats.',
        'Digital Marketer': 'Promote products using digital channels.',
        'Cloud Engineer': 'Manage cloud infrastructure and services.'
    }

    skills = {
        'Software Developer': ['Python', 'Java', 'Algorithms'],
        'Data Analyst': ['Excel', 'SQL', 'Statistics'],
        'UI/UX Designer': ['Adobe XD', 'Sketch', 'Creativity'],
        'Cybersecurity Expert': ['Network Security', 'Cryptography', 'Ethical Hacking'],
        'Digital Marketer': ['SEO', 'Content Creation', 'Google Analytics'],
        'Cloud Engineer': ['AWS', 'Docker', 'Networking']
    }

    roadmap = {
        'Software Developer': 'Start with programming basics → Build projects → Learn frameworks',
        'Data Analyst': 'Learn Excel and SQL → Practice data visualization → Understand statistics',
        'UI/UX Designer': 'Study design principles → Create wireframes → Build portfolios',
        'Cybersecurity Expert': 'Learn networking basics → Study security protocols → Practice hacking labs',
        'Digital Marketer': 'Understand marketing basics → Use SEO tools → Manage campaigns',
        'Cloud Engineer': 'Learn cloud concepts → Get certified (AWS) → Manage real cloud projects'
    }

    return best_role, descriptions[best_role], skills[best_role], roadmap[best_role]
