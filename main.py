from flask import Flask, render_template_string
from flask import Response
import time

app = Flask(__name__)

# HTML шаблон с красным стилем и анимацией
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Село Илек</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #2a0000 0%, #4a0000 50%, #6b0000 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            margin: 0;
        }
        
        .container {
            max-width: 1200px;
            width: 100%;
            position: relative;
        }
        
        /* Стили для заставки разработчика */
        .splash-screen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #1a0000, #3a0000, #5a0000);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 1000;
            animation: fadeOut 1s ease forwards;
            animation-delay: 1s;
            box-shadow: 0 0 50px rgba(255, 0, 0, 0.5);
        }
        
        @keyframes fadeOut {
            0% {
                opacity: 1;
                visibility: visible;
            }
            99% {
                opacity: 0;
                visibility: visible;
            }
            100% {
                opacity: 0;
                visibility: hidden;
            }
        }
        
        .developer-text {
            font-size: 3rem;
            font-weight: bold;
            color: #fff;
            text-shadow: 0 0 20px #ff0000, 0 0 40px #ff4444, 0 0 60px #ff8888;
            animation: pulse 2s infinite;
            text-align: center;
            padding: 20px;
            border: 3px solid #ff4444;
            border-radius: 20px;
            background: rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(10px);
            box-shadow: 0 0 50px rgba(255, 0, 0, 0.7);
        }
        
        @keyframes pulse {
            0%, 100% {
                transform: scale(1);
                opacity: 1;
            }
            50% {
                transform: scale(1.05);
                opacity: 0.9;
            }
        }
        
        /* Стили главной страницы */
        .main-content {
            background: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(10px);
            border-radius: 30px;
            padding: 40px;
            box-shadow: 0 0 50px rgba(255, 0, 0, 0.5);
            border: 2px solid #ff4444;
            color: #fff;
            opacity: 0;
            animation: appear 1s ease forwards;
            animation-delay: 4.5s;
        }
        
        @keyframes appear {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        h1 {
            font-size: 2.5rem;
            color: #ff6666;
            text-shadow: 0 0 15px #ff0000;
            margin-bottom: 20px;
            border-bottom: 3px solid #ff4444;
            padding-bottom: 15px;
        }
        
        p {
            font-size: 1.2rem;
            line-height: 1.6;
            margin-bottom: 20px;
            color: #ffdddd;
        }
        
        .highlight {
            color: #ff8888;
            font-weight: bold;
            text-shadow: 0 0 10px #ff0000;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 30px 0;
            background: rgba(0, 0, 0, 0.5);
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 0 30px rgba(255, 0, 0, 0.3);
        }
        
        th {
            background: #8b0000;
            color: white;
            padding: 15px;
            font-size: 1.1rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            text-shadow: 0 0 10px #ff0000;
        }
        
        td {
            padding: 12px 15px;
            border-bottom: 1px solid #8b0000;
            color: #ffe6e6;
        }
        
        tr:last-child td {
            border-bottom: none;
        }
        
        tr:hover {
            background: rgba(139, 0, 0, 0.3);
            transition: 0.3s;
        }
        
        .info-section {
            margin-top: 30px;
            padding: 20px;
            background: rgba(100, 0, 0, 0.3);
            border-radius: 15px;
            border-left: 5px solid #ff4444;
        }
        
        .info-section p {
            margin-bottom: 15px;
        }
        
        .info-section p:last-child {
            margin-bottom: 0;
        }
        
        /* Анимация появления контента */
        .fade-in {
            animation: fadeInContent 1s ease;
        }
        
        @keyframes fadeInContent {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Красивые красные акценты */
        ::selection {
            background: #ff0000;
            color: white;
        }
        
        /* Адаптивность */
        @media (max-width: 768px) {
            .developer-text {
                font-size: 2rem;
            }
            
            h1 {
                font-size: 2rem;
            }
            
            table {
                font-size: 0.9rem;
            }
            
            td, th {
                padding: 8px;
            }
        }
    </style>
</head>
<body>
    <!-- Заставка с разработчиком -->
    <div class="splash-screen" id="splash">
        <div class="developer-text">
            Разработчик сайта<br>
            <span style="font-size: 4rem; color: #ff4444;">Марейчев Матвей</span>
        </div>
    </div>
    
    <div class="container">
        <!-- Главный контент -->
        <div class="main-content" id="mainContent">
            <h1>Село Илек – административный центр в Илекском районе</h1>
            
            <p><span class="highlight">Население села Илек</span> составляет около 11.000 человек на 24 февраля 2026г.</p>
            
            <p>Село Илек играет важную роль в жизни района, объединяя жителей и обеспечивая их необходимыми условиями для работа и проживания.</p>
            
            <table>
                <thead>
                    <tr>
                        <th>Категория населения</th>
                        <th>Численность населения</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Дети до 6 лет</td>
                        <td>1099 чел.</td>
                    </tr>
                    <tr>
                        <td>Подростки от 7 до 17 лет</td>
                        <td>1309 чел.</td>
                    </tr>
                    <tr>
                        <td>Молодежь от 18 до 29 лет</td>
                        <td>1320 чел.</td>
                    </tr>
                    <tr>
                        <td>Взрослые от 30 до 59 лет</td>
                        <td>4757 чел.</td>
                    </tr>
                    <tr>
                        <td>Пожилые 60 лет и старше</td>
                        <td>2564 чел.</td>
                    </tr>
                    <tr style="background: rgba(139, 0, 0, 0.5); font-weight: bold;">
                        <td>Общее</td>
                        <td>11049 чел.</td>
                    </tr>
                </tbody>
            </table>
            
            <div class="info-section">
                <p>В Илеке функционируют несколько школ и детских садов, обеспечивающих образование для подрастающего поколения. Также в селе работают учреждения культуры, включая Дом культуры и библиотеку, где проводятся различные мероприятия для жителей всех возрастов.</p>
                
                <p>Медицинскую помощь населению оказывает районная больница, оснащенная необходимым оборудованием. Экономика села представлена предприятиями сельского хозяйства и торговли, что создает рабочие места и способствует развитию инфраструктуры.</p>
                
                <p>Благодаря своему расположению на берегу реки Урал, Илек также привлекает туристов и любителей рыбалки, что добавляет разнообразие в жизнь местного сообщества.</p>
            </div>
        </div>
    </div>
    
    <script>
        // Дополнительный скрипт для гарантированного скрытия заставки через 5 секунд
        document.addEventListener('DOMContentLoaded', function() {
            setTimeout(function() {
                const splash = document.getElementById('splash');
                if (splash) {
                    splash.style.opacity = '0';
                    splash.style.visibility = 'hidden';
                }
            }, 5000);
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
