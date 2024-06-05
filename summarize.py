import nltk
from collections import Counter
from nltk.tokenize import word_tokenize, sent_tokenize
from wordcloud import WordCloud
from Control.FileControl import read_file

nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('punkt')

def summarize_file_by_word_frequency(file_path, summary_length=5):
    """
    단어 빈도를 기준으로 점수가 가장 높은 문장으로 파일의 내용을 요약합니다.

    Args:
    file_path(str): 요약할 파일의 경로입니다.
    summary_length(int): 요약의 문장 수. 기본값은 5입니다.

    반환:
    str: 파일 내용 요약입니다.
    """
    try:
        file_contents = read_file(file_path)

        words = word_tokenize(file_contents)
        sentences = sent_tokenize(file_contents)

        words = [word.lower() for word in words if word.isalnum()]
        word_freq = Counter(words)

        sentence_scores = {}
        for sentence in sentences:
            sentence_words = word_tokenize(sentence.lower())
            score = sum(word_freq[word] for word in sentence_words if word in word_freq)
            sentence_scores[sentence] = score

        top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:summary_length]
        summary = ' '.join(top_sentences)

        return summary
    except Exception as e:
        return f"An error occurred: {e}"
    
def generate_wordcloud(file_path, output_path):
    """
    파일의 내용에서 워드 클라우드 이미지를 생성하여 지정된 출력 경로에 저장합니다.
    (한국어도 요약하기 위해선 여러 라이브러리를 설치해야 되서 현재는 영어 파일만 지원합니다.)

    Args:
    file_path(str): 요약할 파일의 경로입니다.
    output_path(str): 워드 클라우드 이미지를 저장할 경로입니다.

    반환:
    None.
    """
    try:
        file_contents = read_file(file_path)

        words = word_tokenize(file_contents)
        words = [word.lower() for word in words if word.isalnum()]

        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word not in stop_words]
        text = ' '.join(words)

        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        wordcloud.to_file(f"{output_path}.png")
        
        print(f"Word cloud image saved to {output_path}.png")
    except Exception as e:
        print(f"An error occurred: {e}")