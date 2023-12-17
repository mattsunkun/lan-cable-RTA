
# lxml必要
from bs4 import BeautifulSoup

class Transcription():

    def __init__(self, strMltSrcPath: str, strMltDstPath) -> None:

        with open(strMltSrcPath, "r") as fp:
            self.soup = BeautifulSoup(fp, features="xml")

        self.strMltDstPath = strMltDstPath

    def marginPlayList(self, strPlayListId: str, strMargin: str) -> None:
        # ターゲット
        playList = self.soup.find("playlist", id=strPlayListId)
        # entryタグ
        entryTags = playList.find_all("entry")
        for i in range(len(entryTags)-1):
            newTagBlank = self.soup.new_tag('blank', length=strMargin)
            entryTags[i].insert_after(newTagBlank)
        
        # blank = self.soup.new_tag("blank", )
        # blank.string = 'This is a new paragraph.'
        # playList.append(new_paragraph)

        # 変更が加えられたHTMLを出力
        modified_html = self.soup.prettify()

        # 出力
        print(modified_html)

    def putSubtitle(self, strSubtitlePath:str, intStartNum: int, intEndNum: int) -> None:


if __name__ == "__main__":
    strMlt = "./experiment_jackfes-2023.mlt"
    strDst = "./test.mlt"
    t = Transcription(strMlt, strDst)
    t.marginPlayList("playlist5", "00:00:00.400")
