-- 테이블 순서는 관계를 고려하여 한 번에 실행해도 에러가 발생하지 않게 정렬되었습니다.

-- jhta_user Table Create SQL
CREATE TABLE jhta_user
(
    user_id     VARCHAR2(20)     NOT NULL, 
    user_idx    NUMBER(18, 0)    NOT NULL, 
    pwd         VARCHAR2(20)     NOT NULL, 
    name        VARCHAR2(20)     NOT NULL, 
    birth       VARCHAR2(20)     NOT NULL, 
    tel         VARCHAR2(20)     NOT NULL, 
    grade       NUMBER(18, 0)    DEFAULT 1 NOT NULL, 
    CONSTRAINT JHTA_USER_PK PRIMARY KEY (user_id)
)
/

CREATE SEQUENCE jhta_user_SEQ
START WITH 1
INCREMENT BY 1;
/

CREATE OR REPLACE TRIGGER jhta_user_AI_TRG
BEFORE INSERT ON jhta_user 
REFERENCING NEW AS NEW FOR EACH ROW 
BEGIN 
    SELECT jhta_user_SEQ.NEXTVAL
    INTO :NEW.user_idx
    FROM DUAL;
END;
/

--DROP TRIGGER jhta_user_AI_TRG;
/

--DROP SEQUENCE jhta_user_SEQ;
/

COMMENT ON TABLE jhta_user IS '사용자'
/

COMMENT ON COLUMN jhta_user.user_id IS '아이디'
/

COMMENT ON COLUMN jhta_user.user_idx IS '인덱스'
/

COMMENT ON COLUMN jhta_user.pwd IS '패스워드'
/

COMMENT ON COLUMN jhta_user.name IS '이름'
/

COMMENT ON COLUMN jhta_user.birth IS '생일'
/

COMMENT ON COLUMN jhta_user.tel IS '전화번호'
/

COMMENT ON COLUMN jhta_user.grade IS '등급'
/


-- jhta_user Table Create SQL
CREATE TABLE restaurant
(
    r_idx          NUMBER(18, 0)    NOT NULL, 
    r_name         VARCHAR2(20)     NULL, 
    r_category     VARCHAR2(20)     NULL, 
    price          NUMBER(18, 0)    NULL, 
    image_url      VARCHAR2(200)    NULL, 
    distance       FLOAT            NULL, 
    score          FLOAT            NULL, 
    site_score     FLOAT            NULL, 
    review         NUMBER(18, 0)    NULL, 
    site_review    NUMBER           NULL, 
    main_menu      VARCHAR2(150)    NULL, 
    CONSTRAINT RESTAURANT_PK PRIMARY KEY (r_idx)
)
/

CREATE SEQUENCE restaurant_SEQ
START WITH 1
INCREMENT BY 1;
/

CREATE OR REPLACE TRIGGER restaurant_AI_TRG
BEFORE INSERT ON restaurant 
REFERENCING NEW AS NEW FOR EACH ROW 
BEGIN 
    SELECT restaurant_SEQ.NEXTVAL
    INTO :NEW.r_idx
    FROM DUAL;
END;
/

--DROP TRIGGER restaurant_AI_TRG;
/

--DROP SEQUENCE restaurant_SEQ;
/

COMMENT ON TABLE restaurant IS '식당'
/

COMMENT ON COLUMN restaurant.r_idx IS '인덱스'
/

COMMENT ON COLUMN restaurant.r_name IS '식당명'
/

COMMENT ON COLUMN restaurant.r_category IS '카테고리'
/

COMMENT ON COLUMN restaurant.price IS '가격'
/

COMMENT ON COLUMN restaurant.image_url IS '이미지 주소'
/

COMMENT ON COLUMN restaurant.distance IS '거리'
/

COMMENT ON COLUMN restaurant.score IS '평점'
/

COMMENT ON COLUMN restaurant.site_score IS '사이트 점수'
/

COMMENT ON COLUMN restaurant.review IS '리뷰수'
/

COMMENT ON COLUMN restaurant.site_review IS '사이트 리뷰수'
/

COMMENT ON COLUMN restaurant.main_menu IS '대표메뉴'
/


-- jhta_user Table Create SQL
CREATE TABLE restaurant_menu
(
    m_idx           NUMBER           NOT NULL, 
    r_idx           NUMBER           NULL, 
    menu            VARCHAR2(100)    NULL, 
    price           NUMBER           NULL, 
    discount        NUMBER           NULL, 
    discount_per    NUMBER           NULL, 
    menu_option     VARCHAR2(100)    NULL, 
    CONSTRAINT RESTAURANT_MENU_PK PRIMARY KEY (m_idx)
)
/

CREATE SEQUENCE restaurant_menu_SEQ
START WITH 1
INCREMENT BY 1;
/

CREATE OR REPLACE TRIGGER restaurant_menu_AI_TRG
BEFORE INSERT ON restaurant_menu 
REFERENCING NEW AS NEW FOR EACH ROW 
BEGIN 
    SELECT restaurant_menu_SEQ.NEXTVAL
    INTO :NEW.m_idx
    FROM DUAL;
END;
/

--DROP TRIGGER restaurant_menu_AI_TRG;
/

--DROP SEQUENCE restaurant_menu_SEQ;
/

COMMENT ON TABLE restaurant_menu IS '메뉴'
/

COMMENT ON COLUMN restaurant_menu.m_idx IS '메뉴번호'
/

COMMENT ON COLUMN restaurant_menu.r_idx IS '식당인덱스'
/

COMMENT ON COLUMN restaurant_menu.menu IS '메뉴명'
/

COMMENT ON COLUMN restaurant_menu.price IS '가격'
/

COMMENT ON COLUMN restaurant_menu.discount IS '할인가'
/

COMMENT ON COLUMN restaurant_menu.discount_per IS '할인율'
/

COMMENT ON COLUMN restaurant_menu.menu_option IS '옵션(1+1, 2+1)'
/

ALTER TABLE restaurant_menu
    ADD CONSTRAINT FK_restaurant_menu_r_idx_resta FOREIGN KEY (r_idx)
        REFERENCES restaurant (r_idx)
/


-- jhta_user Table Create SQL
CREATE TABLE matjip_party
(
    p_idx          NUMBER(18, 0)    NOT NULL, 
    title          VARCHAR2(150)    NULL, 
    user_id        VARCHAR2(20)     NULL, 
    cur_member     NUMBER(18, 0)    NULL, 
    max_member     NUMBER(18, 0)    NULL, 
    mamber_list    VARCHAR2(255)    NULL, 
    status         NUMBER(18, 0)    NULL, 
    CONSTRAINT MATJIP_PARTY_PK PRIMARY KEY (p_idx)
)
/

CREATE SEQUENCE matjip_party_SEQ
START WITH 1
INCREMENT BY 1;
/

CREATE OR REPLACE TRIGGER matjip_party_AI_TRG
BEFORE INSERT ON matjip_party 
REFERENCING NEW AS NEW FOR EACH ROW 
BEGIN 
    SELECT matjip_party_SEQ.NEXTVAL
    INTO :NEW.p_idx
    FROM DUAL;
END;
/

--DROP TRIGGER matjip_party_AI_TRG;
/

--DROP SEQUENCE matjip_party_SEQ;
/

COMMENT ON TABLE matjip_party IS '파티모집'
/

COMMENT ON COLUMN matjip_party.p_idx IS '파티모집번호'
/

COMMENT ON COLUMN matjip_party.title IS '제목'
/

COMMENT ON COLUMN matjip_party.user_id IS '생성자'
/

COMMENT ON COLUMN matjip_party.cur_member IS '현재멤버'
/

COMMENT ON COLUMN matjip_party.max_member IS '최대멤버'
/

COMMENT ON COLUMN matjip_party.mamber_list IS '멤버리스트'
/

COMMENT ON COLUMN matjip_party.status IS '상태'
/

ALTER TABLE matjip_party
    ADD CONSTRAINT FK_matjip_party_user_id_jhta_u FOREIGN KEY (user_id)
        REFERENCES jhta_user (user_id)
/


-- jhta_user Table Create SQL
CREATE TABLE menu_reple
(
    mr_idx      NUMBER          NOT NULL, 
    m_idx       NUMBER          NULL, 
    user_id     VARCHAR2(20)    NULL, 
    reple       VARCHAR2(20)    NULL, 
    score       FLOAT           NULL, 
    rep_time    DATE            NULL, 
    status      NUMBER          NULL, 
    CONSTRAINT MENU_REPLE_PK PRIMARY KEY (mr_idx)
)
/

CREATE SEQUENCE menu_reple_SEQ
START WITH 1
INCREMENT BY 1;
/

CREATE OR REPLACE TRIGGER menu_reple_AI_TRG
BEFORE INSERT ON menu_reple 
REFERENCING NEW AS NEW FOR EACH ROW 
BEGIN 
    SELECT menu_reple_SEQ.NEXTVAL
    INTO :NEW.mr_idx
    FROM DUAL;
END;
/

--DROP TRIGGER menu_reple_AI_TRG;
/

--DROP SEQUENCE menu_reple_SEQ;
/

COMMENT ON TABLE menu_reple IS '메뉴 댓글'
/

COMMENT ON COLUMN menu_reple.mr_idx IS '댓글번호'
/

COMMENT ON COLUMN menu_reple.m_idx IS '메뉴번호'
/

COMMENT ON COLUMN menu_reple.user_id IS '유저아이디'
/

COMMENT ON COLUMN menu_reple.reple IS '내용'
/

COMMENT ON COLUMN menu_reple.score IS '점수'
/

COMMENT ON COLUMN menu_reple.rep_time IS '시간'
/

COMMENT ON COLUMN menu_reple.status IS '상태'
/

ALTER TABLE menu_reple
    ADD CONSTRAINT FK_menu_reple_m_idx_restaurant FOREIGN KEY (m_idx)
        REFERENCES restaurant_menu (m_idx)
/

ALTER TABLE menu_reple
    ADD CONSTRAINT FK_menu_reple_user_id_jhta_use FOREIGN KEY (user_id)
        REFERENCES jhta_user (user_id)
/


-- jhta_user Table Create SQL
CREATE TABLE restaurant_reple
(
    rr_idx      NUMBER          NOT NULL, 
    r_idx       NUMBER          NULL, 
    user_id     VARCHAR2(20)    NULL, 
    reple       VARCHAR2(20)    NULL, 
    score       FLOAT           NULL, 
    rep_time    DATE            NULL, 
    status      NUMBER          NULL, 
    CONSTRAINT RESTAURANT_REPLE_PK PRIMARY KEY (rr_idx)
)
/

CREATE SEQUENCE restaurant_reple_SEQ
START WITH 1
INCREMENT BY 1;
/

CREATE OR REPLACE TRIGGER restaurant_reple_AI_TRG
BEFORE INSERT ON restaurant_reple 
REFERENCING NEW AS NEW FOR EACH ROW 
BEGIN 
    SELECT restaurant_reple_SEQ.NEXTVAL
    INTO :NEW.rr_idx
    FROM DUAL;
END;
/

--DROP TRIGGER restaurant_reple_AI_TRG;
/

--DROP SEQUENCE restaurant_reple_SEQ;
/

COMMENT ON TABLE restaurant_reple IS '식당 댓글'
/

COMMENT ON COLUMN restaurant_reple.rr_idx IS '댓글번호'
/

COMMENT ON COLUMN restaurant_reple.r_idx IS '식당번호'
/

COMMENT ON COLUMN restaurant_reple.user_id IS '유저아이디'
/

COMMENT ON COLUMN restaurant_reple.reple IS '내용'
/

COMMENT ON COLUMN restaurant_reple.score IS '점수'
/

COMMENT ON COLUMN restaurant_reple.rep_time IS '시간'
/

COMMENT ON COLUMN restaurant_reple.status IS '상태'
/

ALTER TABLE restaurant_reple
    ADD CONSTRAINT FK_restaurant_reple_r_idx_rest FOREIGN KEY (r_idx)
        REFERENCES restaurant (r_idx)
/

ALTER TABLE restaurant_reple
    ADD CONSTRAINT FK_restaurant_reple_user_id_jh FOREIGN KEY (user_id)
        REFERENCES jhta_user (user_id)
/


-- jhta_user Table Create SQL
CREATE TABLE party_reple
(
    pr_idx      NUMBER(18, 0)    NOT NULL, 
    p_idx       NUMBER(18, 0)    NULL, 
    user_id     VARCHAR2(20)     NULL, 
    reple       VARCHAR2(255)    NULL, 
    rep_time    DATE             NULL, 
    status      NUMBER(18, 0)    NULL, 
    CONSTRAINT PARTY_REPLE_PK PRIMARY KEY (pr_idx)
)
/

CREATE SEQUENCE party_reple_SEQ
START WITH 1
INCREMENT BY 1;
/

CREATE OR REPLACE TRIGGER party_reple_AI_TRG
BEFORE INSERT ON party_reple 
REFERENCING NEW AS NEW FOR EACH ROW 
BEGIN 
    SELECT party_reple_SEQ.NEXTVAL
    INTO :NEW.pr_idx
    FROM DUAL;
END;
/

--DROP TRIGGER party_reple_AI_TRG;
/

--DROP SEQUENCE party_reple_SEQ;
/

COMMENT ON TABLE party_reple IS '파티댓글'
/

COMMENT ON COLUMN party_reple.pr_idx IS '팟댓글번호'
/

COMMENT ON COLUMN party_reple.p_idx IS '파티번호'
/

COMMENT ON COLUMN party_reple.user_id IS '유저아이디'
/

COMMENT ON COLUMN party_reple.reple IS '댓글'
/

COMMENT ON COLUMN party_reple.rep_time IS '단 시간'
/

COMMENT ON COLUMN party_reple.status IS '상태'
/

ALTER TABLE party_reple
    ADD CONSTRAINT FK_party_reple_p_idx_matjip_pa FOREIGN KEY (p_idx)
        REFERENCES matjip_party (p_idx)
/

ALTER TABLE party_reple
    ADD CONSTRAINT FK_party_reple_user_id_jhta_us FOREIGN KEY (user_id)
        REFERENCES jhta_user (user_id)
/


